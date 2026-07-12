# Active Directory Attack Lab

A complete hands-on Active Directory lab that demonstrates how common Active Directory attacks are performed, how they work internally, and how they can be mitigated.

> ⚠️ **Disclaimer**
>
> This project was created for educational purposes only inside an isolated virtual lab environment. It is intended to help security professionals, students, and defenders understand Active Directory attack techniques and corresponding mitigations.

---

# Project Overview

This project simulates a realistic enterprise Active Directory environment (EvilCorp.local) containing multiple workstations, servers, users, organizational units, and services.

The objective is to understand how attackers compromise Windows domains by abusing authentication protocols, Active Directory misconfigurations, credential attacks, and lateral movement techniques.

Each attack includes:

- Attack overview
- Prerequisites
- Internal protocol explanation
- Step-by-step execution
- Screenshots

---

# Lab Infrastructure

The environment consists of:

- Domain Controller
- IIS Web Server
- HR Workstation
- IT Workstation
- Management Workstation
- Hacker Machine
## Lab Architecture

![Lab Architecture](Images/Architecture.png)

---

# Demonstrated Attacks

- Password Brute Force
- Password Spraying
- AS-REP Roasting
- Kerberoasting
- Pass-the-Hash
- Overpass-the-Hash
- Pass-the-Ticket
- Silver Ticket
- Golden Ticket
- DCSync
- DCShadow
- Lateral Movement
  - WMI
  - WinRM
  - PsExec
  - DCOM

---

# Topics Covered

- Active Directory Administration
- Kerberos Authentication
- NTLM Authentication
- LDAP Enumeration
- Service Principal Names (SPNs)
- Kerberos Tickets (TGT & TGS)
- LSASS Credential Dumping
- Active Directory Replication
- Windows Remote Management
- Windows Management Instrumentation
- SMB
- DCOM

---

# Tools Used

### Offensive Security

- Mimikatz
- Rubeus
- PowerView
- CrackMapExec
- Evil-WinRM
- Impacket
- PsExec

### Password Cracking

- Hashcat
- RockYou Wordlist

### Enumeration

- PowerShell
- LDAP
- ADSI
- Custom Enumeration Script

### Windows

- Process Hacker
- Klist
- IIS
- Active Directory Users and Computers
- DNS Manager
- Group Policy Management

---

# Learning Objectives

This lab demonstrates:

- How Active Directory authentication works
- Kerberos internals
- Credential theft techniques
- Kerberos ticket attacks
- Credential replay attacks
- Active Directory replication abuse
- Remote administration abuse
- Lateral movement
- Privilege escalation
- Persistence techniques
- Defensive mitigations

---

# Repository Structure

```
Active-Directory-Lab/
│
├── Documentation/
│   ├── Project Overview
│   ├── Lab Setup
│   ├── Authentication
│   ├── Credential Attacks
│   ├── Kerberos Attacks
│   ├── Lateral Movement
│   └── Mitigations
│
├── Images/
│
├── Scripts/
│
├── Tools/
│
└── README.md
```

---

# Skills Demonstrated

- Active Directory
- Windows Administration
- Offensive Security
- Red Team
- Kerberos
- NTLM
- LDAP
- PowerShell
- Windows Internals
- Authentication Protocols
- Privilege Escalation
- Lateral Movement
- Persistence
- Credential Access

---

# MITRE ATT&CK Coverage

This project covers techniques from multiple MITRE ATT&CK tactics, including:

- Initial Access
- Credential Access
- Discovery
- Lateral Movement
- Privilege Escalation
- Persistence
- Defense Evasion

---

# Author

**Samuel Adham**

Communication & Electronics Engineer

Cybersecurity | Active Directory Security | Red Team | Windows Internals

---

⭐ If you found this project useful, consider giving the repository a star.
