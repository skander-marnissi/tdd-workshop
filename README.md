## Why Was My Repository Moved to Private?

If your repository has been moved to private and you're unsure why, don’t worry! This change is part of new security policies designed to protect sensitive data and comply with external audit requirements.

### What Triggers This Action?

Your repository may have been flagged for one or more of the following reasons:

1. **Presence of Highly Sensitive Data**  
   The repository contains unencrypted sensitive information, such as:  
   - Identification credentials  
   - API secrets or tokens  

2. **Classified Code**  
   The repository includes code classified as:  
   - **C2 or C3 levels**, as per internal security classification standards.

### Why Was This Necessary?

This action is taken to prevent serious risks that may arise from unprotected repositories, such as:  
- **Sensitive Information Leaking**: Unintended exposure of credentials or classified data.  
- **Data Alteration**: Unauthorized changes to critical data or code.  
- **Rogue Trading**: Exploitation of unsecure repositories to manipulate systems maliciously.  
- **Payment System Fraud**: Potential misuse of financial operations or transaction data.

These steps are aligned with **ECB audit requirements** and broader security policies around continuous integration tools. To ensure compliance and safeguard critical information, repositories meeting the above criteria are automatically set to private.

If you have further questions or need assistance, feel free to contact our support team.
