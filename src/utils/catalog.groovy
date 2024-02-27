/*
 * functions as a basic catalog query service for MB file-level datasets. Returns the information necessary to construct
 * an S3 object name for the selected files as well as attributes necessary for MB-System mbgrid datalist
 *
 */
// "https://www.ngdc.noaa.gov/next-catalogs/rest/autogrid/catalog/file?geometry=${params.geometry}&gridCellSize=30"

import groovy.json.*
import groovy.sql.*

if (! params.geometry || validateGeometry(params.geometry) == false) {
    response.status = 400
    println 'Error: invalid or missing parameter "geometry"'
    return
}

def configFile = new File(context.getInitParameter('configfile'))
assert configFile.exists()
def config = new ConfigSlurper().parse(configFile.toURL())

def driver = 'oracle.jdbc.OracleDriver'

//def sql = Sql.newInstance(config.database.url, config.cruise.database.user, config.cruise.database.password, driver)
def sql = Sql.newInstance(config.database.url, config.multibeam.database.user, config.multibeam.database.password, driver)

def acceptableParameters = [
   'DATE': '''END_TIME >= TO_DATE(SUBSTR(?, 1, 10), 'YYYY-MM-DD')''',
   'INGEST_DATE': '''ENTERED_DATE >= TO_DATE(SUBSTR(?, 1, 10), 'YYYY-MM-DD')''',
   'SURVEY': 'SURVEY_NAME = ?',
   'PLATFORM': 'SHIP_NAME = ?',
   'DATA_PROVIDER': 'SOURCE = ?',
   'INSTRUMENT': 'INSTRUMENT = ?'
]

def criteria = []
def values = []
params.each { k,v ->

    key = k.toUpperCase()
    //ignore criteria where a value is falsey
    if (v && acceptableParameters[key]) {
        criteria.push(acceptableParameters[key])
        values.push(v)
    }
}
def criteriaClause = criteria.size() ? ' and ' + criteria.join(' and '): ''

response.contentType = 'text/plain'

//def query = '''select DATA_FILE,MBIO_FORMAT_ID from CRUISE.MBINFO_FILE_TSQL a
def query = """select DATA_FILE,MBIO_FORMAT_ID from MB_READ.MBINFO_FILE_TSQL a, MB_READ.SURVEY b
where a.ngdc_id = b.ngdc_id and
SDO_RELATE(
    a.SHAPE,
    MDSYS.SDO_GEOMETRY(
       2003,
       8307,
       null,
       mdsys.sdo_elem_info_array(1,1003,3),
       mdsys.sdo_ordinate_array(?,?,?,?)),
    'mask=anyinteract querytype=window'
) = 'TRUE' ${criteriaClause} order by DATA_FILE"""
List coords = params.geometry.split(',').collect { it.toDouble() }

try {
    sql.eachRow(query,coords+values) { row ->
        def filename = row[0]
        if (filename.endsWith('.gz')) {
            filename = filename.substring(0, filename.lastIndexOf('.gz'))
            print "/mgg/MB/${filename}.fbt 71\n"        //"71" is FBT
        } else {
            //assume fbt not available, use raw multibeam instead
            print "/mgg/MB/${filename} ${row[1]}\n"
        }
    }
} catch (e) {
    response.status = 500
    println e
    println "Error: unable to connect to server"
} finally {
    sql.close()
}


Boolean validateGeometry(geom){
    List coords = geom.split(',')
    if (coords.size() != 4) { return false }
    //use isDouble()?
    if (! coords.every { it.isNumber() }) { return false }

    coords = coords.collect { it.toDouble() }
    if (coords[0] < -180 || coords[1] < -90 || coords[2] > 180 || coords[3] > 90) { return false }

    return true
}
