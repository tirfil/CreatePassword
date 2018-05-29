# CreatePassword
Create really different passwords to connect to your internet websites.

Security rules require to have strong password.

On internet, most of websites needs login credentials to connect.

Users lend to use the same password (with or without variation) as login credentials.

If a unsecure website is compromised and login/password file read , hackers can easily guess password for others websites with more sensible informations.

This program (python or html/javascript version available), create strong password (at least one figure, one upper case, one lower case, special character ...) based on a primary password and a website id.

Using the same primary password , you are able to generate different complex passwords for your website. 

You need only to remember your primary password to retreive the strong password for all your website.

*Principle:*
After concatenation of website id and the primary password , an hash value (sha256) is computed.
bytes extracted from hash value enable to generate a strong password.


Examples:

amazon + hello123 -> Q0>q23G5sPPG

ebay + hello123   -> H8*whjkk6Aat

paypal + hello123 -> V4(cbtbhrhUh

...



