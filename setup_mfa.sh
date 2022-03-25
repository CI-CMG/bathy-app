#!/bin/bash

# Function to clear current STS configuration.
#
# Use this to reset your session to your static AWS_PROFILE configuration
# removing any time-limited temporary credentials from your environment
function unset-sts() {
  unset AWS_ACCESS_KEY_ID;
  unset AWS_SECRET_ACCESS_KEY;
  unset AWS_SESSION_TOKEN;
  unset AWS_MFA_EXPIRY;
  unset AWS_SESSION_EXPIRY;
  unset AWS_ROLE;
}

# Authenticate with an MFA Token Code
function mfa() {

  # Remove any environment variables previously set by sts()
  unset-sts;

  # Get AWS profile
  #
  # Can either provide a profile name as an argument or set the AWS_DEFAULT_PROFILE env var
  profile="${1:-default}"

  # Get MFA Serial
  #
  # Assumes "iam list-mfa-devices" is permitted without MFA
  mfa_serial="$(aws --profile ${profile} iam list-mfa-devices --query 'MFADevices[*].SerialNumber' --output text)";
  if ! [ "${?}" -eq 0 ]; then
    echo "Failed to retrieve MFA serial number" >&2;
    return 1;
  fi;

  # Read the token from the console
  echo -n "MFA Token Code: ";
  read token_code;

  # Call STS to get the session credentials
  #
  # Assumes "sts get-session-token" is permitted without MFA
  read AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN <<< $(aws --profile ${profile} sts get-session-token --serial-number $mfa_serial --duration 129600 --output text --token-code $token_code | awk '{ print $2, $4, $5 }')

  # Set the environment credentials specifically for this command
  # and execute the command
  export AWS_ACCESS_KEY_ID
  export AWS_SECRET_ACCESS_KEY
  export AWS_SESSION_TOKEN
  export AWS_MFA_EXPIRY

  if [[ -n "${AWS_ACCESS_KEY_ID}" && -n "${AWS_SECRET_ACCESS_KEY}" && -n "${AWS_SESSION_TOKEN}" ]]; then
    aws --profile mfa configure set aws_access_key_id "$AWS_ACCESS_KEY_ID"
    aws --profile mfa configure set aws_secret_access_key "$AWS_SECRET_ACCESS_KEY"
    aws --profile mfa configure set aws_session_token "$AWS_SESSION_TOKEN"
    aws --profile mfa configure set region $(aws --profile $profile configure get region)
    echo "MFA Succeeded. With great power comes great responsibility...";
    return 0;
  else
    echo "MFA Failed" >&2;
    return 1;
  fi;
}

mfa "nesdis"
