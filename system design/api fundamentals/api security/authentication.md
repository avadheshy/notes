# Authentication & Authorization

# 1. Introduction
In any system that involves users and data, access control is not just a feature, it's a foundational requirement. Without it, there's nothing to stop anyone from accessing sensitive information or performing destructive actions. This is where authentication and authorization come in.

Think of it like visiting a secure office building:

Authentication is showing your ID badge at the front desk to prove you are an employee. The system verifies who you are.

Authorization is what happens next. Your ID badge determines which floors and rooms you can access. The system decides what you can do.

Both are essential. Without authentication, anyone can walk in. Without authorization, every authenticated employee could access the CEO's office. They are distinct but interdependent processes that form the bedrock of secure system design.

# 2. What Is Authentication?
Authentication is the process of verifying a user's claimed identity. It answers the question, "Are you really who you say you are?" This is typically done by challenging the user to provide proof of their identity, which can come in several forms:

Something you know: A password, PIN, or secret answer.

Something you have: A physical token, a mobile phone (for OTPs), or a smart card.

Something you are: A biometric factor like a fingerprint, face scan, or retina scan.

Modern systems often combine these through Multi-Factor Authentication (MFA) to increase security.

## Common Authentication Methods

## Authentication Types

| Type                         | Description                                                      | Example                      |
|------------------------------|------------------------------------------------------------------|------------------------------|
| **Basic Auth**               | Credentials (username/password) sent with every request.        | Legacy APIs                  |
| **Session-Based Auth**       | Server issues session ID stored in cookies.                     | Traditional web apps         |
| **Token-Based Auth (JWT)**   | Stateless tokens (e.g., JWT) passed in headers.                 | REST APIs                    |
| **OAuth 2.0**                | Delegated access between services.                              | "Sign in with Google"        |
| **Passwordless / Biometric** | Email links or biometrics replace passwords.                    | Magic link login, Face ID    |

# 3. What Is Authorization?
Authorization is the process of determining whether an authenticated user has the necessary permissions to perform a specific action or access a particular resource. It happens after successful authentication and answers the question, "Is this user allowed to do this?"

Authorization decisions are made by an access policy engine based on a set of rules.

## Common Authorization Models
## Access Control Models

| Model                                  | Description                                                         | Example                                              |
|----------------------------------------|---------------------------------------------------------------------|------------------------------------------------------|
| **RBAC (Role-Based Access Control)**  | Permissions grouped into roles.                                     | Admin, Editor, Viewer                                |
| **ABAC (Attribute-Based Access Control)** | Access based on attributes like user, resource, or context.     | "Allow if user.department == resource.department"    |
| **PBAC (Policy-Based Access Control)** | Uses declarative policies for fine-grained control.                | AWS IAM, OPA                                         |

**Role-Based Access Control (RBAC)**: Permissions are assigned to roles (e.g., admin, editor), and users are assigned to roles.

**Attribute-Based Access Control (ABAC)**: Permissions are based on attributes of the user, resource, and environment (e.g., "Allow users in the 'Marketing' department to edit documents they own").

**Policy-Based Access Control (PBAC)**: A more flexible model where rules are defined as explicit policies.

# Security Considerations & Best Practices
Always use HTTPS (TLS): Encrypt all communication to prevent credentials and tokens from being intercepted.

Never store plain passwords: Always hash passwords with a strong, slow algorithm (like Argon2 or bcrypt) and a unique salt for each user.

Use short-lived tokens: Access tokens should have a short expiry time (e.g., 15 minutes), with a long-lived refresh token used to get new ones.

Implement the Principle of Least Privilege: Users should only have the minimum permissions necessary to do their job.

Guard against common attacks: Sanitize inputs, use anti-CSRF tokens for session-based apps, and implement rate limiting on login endpoints.
