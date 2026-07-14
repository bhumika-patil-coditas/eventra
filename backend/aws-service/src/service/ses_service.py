import boto3
from botocore.exceptions import ClientError
from src.core import SETTINGS, LOGGER, CustomException


class SesService:
    def __init__(
        self
    ) -> None:
        self.ses_client = boto3.client(
            "ses",
            region_name=SETTINGS.AWS_REGION,
            aws_access_key_id=SETTINGS.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=SETTINGS.AWS_SECRET_ACCESS_KEY,
        )

    def send_text_mail(
        self,
        to_address: list[str],
        subject: str,
        body_text: str,
        sender_mail: str = SETTINGS.ADMIN_MAIL,
    ) -> str:
        try:
            LOGGER.info(f"Sending the mail to {to_address}")
            response = self.ses_client.send_email(
                Source=sender_mail,
                Destination={"ToAddresses": to_address},
                Message={
                    "Subject": {"Data": subject, "Charset": "UTF-8"},
                    "Body": {"Text": {"Charset": "UTF-8", "Data": body_text}},
                },
            )
            LOGGER.info(
                f"Mail sent successfully to {to_address} : {response['MessageId']}"
            )
            return response["MessageId"]
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            error_message = e.response["Error"]["Message"]
            LOGGER.exception(f"SES error ({error_code}): {error_message}")
            raise CustomException.InternalError(message="Failed to connect to Aws")

    
    def validate_email_address(self, email:str):
        response = self.ses_client.verify_email_identity(
            EmailAddress=email
        )

        return response