import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from django.conf import settings

def send_welcome_email(to_email, recipient_name, reg_id):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    sender = {"email": settings.DEFAULT_FROM_EMAIL, "name": "ScaleUp Conclave"}
    to = [{"email": to_email, "name": recipient_name}]
    template_id = 3  # Replace with your actual template ID in Brevo

    params = {
        "recipient_name": recipient_name,
        "reg_id": reg_id
    }

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        sender=sender,
        template_id=template_id,
        params=params,
    )

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(f"Email sent: {api_response}")
    except ApiException as e:
        print(f"Error sending email: {e}")
        # Optionally raise or handle error here
