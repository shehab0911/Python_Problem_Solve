#3: Generate 6 digit random secure OTP

import secrets
secretsGenerator=secrets.SystemRandom()
otp=secretsGenerator.randrange(100000,999999)
print(otp)

