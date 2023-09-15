import smtplib
import ssl
import os
from email.message import EmailMessage
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
 

def send_email_to_applicant(email,name,title):


    # Set your Gmail email address and password
    gmail_email = os.environ['gmail_email']
    gmail_password = os.environ['gmail_password']

    # Create the email message
    # msg = MIMEMultipart()
    em = EmailMessage()
    em['From'] = gmail_email
    em['To'] = email # Replace with the recipient's email address
    em['Subject'] = "Congratulations on Your Job Approval!"

    # Email body
    body = f"""
Dear {name},

I hope this email finds you well. We are delighted to inform you that your application for the {title} position at Chaynz Tech has been approved, and we would like to extend our warmest congratulations to you!

Your qualifications, experience, and enthusiasm have stood out among our pool of applicants, and we believe that you will be a valuable addition to our team. We were particularly impressed by [mention a specific aspect of their application or interview that impressed the hiring team].

Now that your application has been approved, we kindly request that you complete the following steps to finalize your employment with us:

1. Review and Sign the Employment Offer Letter:
   Attached to this email, you will find your formal offer letter outlining the terms and conditions of your employment. Please review it carefully, sign, and return it to us by [insert deadline]. If you have any questions or require clarification on any aspect of the offer, do not hesitate to reach out to [HR Contact Name] at [HR Contact Email].

2. Complete the Onboarding Process:
   Our HR team will be in touch with you shortly to assist with the onboarding process, including necessary paperwork, background checks, and any required training or orientation. This will ensure a smooth transition into your new role.

3. Coordinate Your Start Date:
   Please let us know your availability to start your new position. We aim to accommodate your preferences as much as possible and ensure a seamless onboarding experience.

Once again, congratulations on your job approval! We look forward to having you join the Chaynz Tech team and are excited about the contributions we know you will make.

If you have any further questions or need assistance with any part of the onboarding process, please feel free to contact us at xyz@gmail.com or +92xxxxxxxxx.

Welcome aboard, {name}, and here's to a successful journey ahead with Chaynz Tech!

Best regards,"""


    # msg.attach(MIMEText(body, 'plain'))
    em.set_content(body)


    # Establish a secure connection with Gmail's SMTP server
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        # try:
            # Login to your Gmail account
            server.login(gmail_email, gmail_password)

            # Send the email
            server.sendmail(gmail_email, email, em.as_string())
            # print("Email sent successfully!")

        # except Exception as e:
        #     print(f"An error occurred: {e}")





# Subject: Congratulations on Your Job Approval!

# Dear [Applicant's Name],

# I hope this email finds you well. We are delighted to inform you that your application for the [Job Title] position at [Company Name] has been approved, and we would like to extend our warmest congratulations to you!

# Your qualifications, experience, and enthusiasm have stood out among our pool of applicants, and we believe that you will be a valuable addition to our team. We were particularly impressed by [mention a specific aspect of their application or interview that impressed the hiring team].

# Now that your application has been approved, we kindly request that you complete the following steps to finalize your employment with us:

# 1. Review and Sign the Employment Offer Letter:
#    Attached to this email, you will find your formal offer letter outlining the terms and conditions of your employment. Please review it carefully, sign, and return it to us by [insert deadline]. If you have any questions or require clarification on any aspect of the offer, do not hesitate to reach out to [HR Contact Name] at [HR Contact Email].

# 2. Complete the Onboarding Process:
#    Our HR team will be in touch with you shortly to assist with the onboarding process, including necessary paperwork, background checks, and any required training or orientation. This will ensure a smooth transition into your new role.

# 3. Coordinate Your Start Date:
#    Please let us know your availability to start your new position. We aim to accommodate your preferences as much as possible and ensure a seamless onboarding experience.

# Once again, congratulations on your job approval! We look forward to having you join the [Company Name] team and are excited about the contributions we know you will make.

# If you have any further questions or need assistance with any part of the onboarding process, please feel free to contact us at [HR Contact Email] or [HR Contact Phone Number].

# Welcome aboard, [Applicant's Name], and here's to a successful journey ahead with [Company Name]!

# Best regards,

# [Your Name]
# [Your Title]
# [Company Name]
# [Email Address]
# [Phone Number]