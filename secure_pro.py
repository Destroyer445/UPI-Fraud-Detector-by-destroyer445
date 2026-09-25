# UPI Secure Guard PRO v2.0 - by destroyer445
import re

print("--- UPI Secure Guard PRO v2.0 ---")
print("Created by destroyer445 | Kerala Cyber Security\n")

upi_input = input("Enter UPI ID / Payment Link to check: ").lower()

# PRO FEATURES
scam_keywords = ["lottery", "reward", "verify", "suspended", "kyc", "urgent", "blocked", "prize", "refund"]
fake_domains = ["gpay-secure", "phonepe-offer", "paytm-kyc", "upi-verify"]

# 1. UPI ID Regex Validation (PRO)
upi_pattern = r"^[a-zA-Z0-9.\-_]{2,256}@[a-zA-Z]{2,64}$"

if "@" in upi_input:
    if re.match(upi_pattern, upi_input):
        print("✅ [PRO] Valid UPI Format Detected")
    else:
        print("❌ [PRO] ALERT: Fake UPI Format! Scammers use weird characters.")
    
    # Scam word check
    for word in scam_keywords:
        if word in upi_input:
            print(f"🚨 [PRO] CRITICAL SCAM ALERT: '{word}' found in UPI ID!")

# 2. Fake Link Detector (PRO)
else:
    if any(domain in upi_input for domain in fake_domains):
        print("🚨 [PRO] FAKE PAYMENT LINK! Original GPay/PhonePe never uses such links")
    if "http" in upi_input and "upi" in upi_input:
        print("⚠️ [PRO] Suspicious Link: Don't click UPI links from unknown persons")

# 3. PRO Safety Score
print("\n--- PRO Safety Score ---")
score = 100
if any(w in upi_input for w in scam_keywords): score -= 70
if not re.match(upi_pattern, upi_input) and "@" in upi_input: score -= 50

if score >= 80: print(f"🟢 Safety Score: {score}/100 - Safe")
elif score >= 50: print(f"🟡 Safety Score: {score}/100 - Be Careful!")
else: print(f"🔴 Safety Score: {score}/100 - DANGER! DO NOT PAY!")

print("\nPRO Tip by destroyer445: Always verify in your UPI app before paying!")
