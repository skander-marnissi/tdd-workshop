    <section>
        <h1><b>Why Was My Repository Moved to Private?</b></h1>
        <p>
            If your repository has been moved to private and you're unsure why, don’t worry! This change is part of new security policies designed to protect sensitive data and comply with external audit requirements.
        </p>
    </section>
    
    <section>
        <h2><b>What Triggers This Action?</b></h2>
        <p>Your repository may have been flagged for one or more of the following reasons:</p>
        <ul>
            <li><b>1. Presence of Highly Sensitive Data</b>
                <ul>
                    <li>The repository contains unencrypted sensitive information, such as:</li>
                    <ul>
                        <li>Identification credentials</li>
                        <li>API secrets or tokens</li>
                    </ul>
                </ul>
            </li>
            <li><b>2. Classified Code</b>
                <ul>
                    <li>The repository includes code classified as:</li>
                    <ul>
                        <li>C2 or C3 levels, according to the ASA/Masai assessment security classification standards.</li>
                    </ul>
                </ul>
            </li>
        </ul>
    </section>

    <section>
        <h2><b>Why Was This Necessary?</b></h2>
        <p>This action is taken to prevent serious risks that may arise from unprotected repositories, such as:</p>
        <ul>
            <li><b>Sensitive Information Leaking:</b> Unintended exposure of credentials or classified data.</li>
            <li><b>Data Alteration:</b> Unauthorized changes to critical data or code.</li>
            <li><b>Rogue Trading:</b> Exploitation of unsecure repositories to manipulate systems maliciously.</li>
            <li><b>Payment System Fraud:</b> Potential misuse of financial operations or transaction data.</li>
        </ul>
        <p>
            These steps are aligned with <b>ECB audit requirements</b> and broader security policies around continuous integration tools. To ensure compliance and safeguard critical information, repositories meeting the above criteria are automatically set to private.
        </p>
        <p>If you have further questions or need assistance, feel free to contact our support team.</p>
    </section>
