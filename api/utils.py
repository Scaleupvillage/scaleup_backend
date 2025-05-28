def send_welcome_email(to_email, recipient_name):
    subject = "Welcome to ScaleUp Conclave Dubai – You're In!"
    message = f"""
Hey {recipient_name},

Congratulations!
You are officially part of ScaleUp Conclave Dubai, the second edition of our premier gathering designed to be a launchpad for startups and a gateway to business networks. This is where ambitious entrepreneurs, industry leaders, and visionaries converge to ignite ideas and accelerate growth.

Event Details:
* Date: June 19, 2025
* Time: 9:00 AM onwards
* Venue: Millennium Airport Hotel, Dubai
  Location: https://maps.app.goo.gl/E6MDEZERAijPKV2E8

This invite is brought to you by ScaleUp Conclave.

See you soon!
"""
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
