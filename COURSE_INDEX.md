# Course Index — Software Security

Source snapshot: **1 October 2026**.

## Course metadata

| Field | Value |
| --- | --- |
| Programme | Software Engineering / Ingineria sistemelor software |
| Year | II |
| Semester | III |
| Course type | Optional |
| Credits | 7 ECTS |
| Weekly contact | 2h course + 2h seminar/laboratory |
| Total contact | 28h course + 28h seminar/laboratory |
| Instructor | Lecturer PhD. Vasile Cătălin Bîrjoveanu |
| Lab attendance | Mandatory |
| Official page | https://edu.info.uaic.ro/securitate-software/ |

## Course topics

1. Set-UID privileged programs and attacks
2. Environment variables and attacks
3. Shellshock
4. Buffer overflows
5. Shellcode injection
6. Return-to-libc
7. Return-oriented programming (ROP)
8. Protection mechanisms against buffer overflows
9. Format-string attacks
10. Race conditions
11. SQL injection
12. Cross-site scripting (XSS)
13. Software-security vulnerabilities and principles

The public 2026 course page frames the subject around the role of software both as a security mechanism and as a source of insecurity, understanding root causes of vulnerabilities, and applying techniques and tools for secure software.

## Attacks laboratory

The laboratory is Linux-oriented and is based on analysing software, finding vulnerabilities, exploiting them in the controlled lab setting, and applying prevention/mitigation techniques.

The official programme lists the following practical sequence:

1. Set-UID privileged programs
2. Attacks on Set-UID privileged programs
3. Attacks through environment variables
4. Shellshock
5. Shellcode injection
6. Shellcode injection — continuation
7. Defeating `dash` protection
8. Return-to-libc
9. Return-to-libc — continuation
10. Format-string attacks
11. Race-condition attacks
12. SQL injection
13. Cross-site scripting
14. Software-security vulnerabilities

## Lecture-note links exposed by the teacher site

| Topic | Official file |
| --- | --- |
| Set-UID privileged programs and attacks | https://edu.info.uaic.ro/securitate-software/Set-UID_Progs_Attacks.pdf |
| Environment variables and attacks | https://edu.info.uaic.ro/securitate-software/Env_Vars_Attacks.pdf |
| Shellshock | https://edu.info.uaic.ro/securitate-software/Sshock.pdf |
| Buffer overflow attacks | https://edu.info.uaic.ro/securitate-software/Buffer%20Overflow.pdf |
| Shellcode injection attacks | https://edu.info.uaic.ro/securitate-software/Scode.pdf |
| Return-to-libc and ROP attacks | https://edu.info.uaic.ro/securitate-software/Return-to-libc.pdf |
| Buffer-overflow protection mechanisms | https://edu.info.uaic.ro/securitate-software/Protections_Buffer%20Overflow.pdf |
| Format-string attacks | https://edu.info.uaic.ro/securitate-software/FString_Attacks.pdf |
| Software-security vulnerabilities | https://edu.info.uaic.ro/securitate-software/SS_Vulnerabilities.pdf |
| Race-condition attacks | https://edu.info.uaic.ro/securitate-software/Race%20Condition.pdf |
| SQL injection attacks | https://edu.info.uaic.ro/securitate-software/SQL%20Injection.pdf |
| Cross-site scripting (XSS) | https://edu.info.uaic.ro/securitate-software/XSS.pdf |

Run `python3 scripts/scrape_course.py` to refresh link discovery from the current teacher page rather than relying only on this snapshot.

## Assessment

According to the published 2025–2026 Software Engineering course programme:

- **Continuous assessment:** 80% of the overall result.
  - Course component: 25% of the continuous assessment; project and case study are weighted equally inside that component.
  - Seminar/laboratory component: 75% of the continuous assessment; continuous practical assessment and case study are weighted equally inside that component.
- **Final assessment:** 20%, described as a final mixed assessment.
- The programme states that both **continuous assessment ≥ 5** and **final assessment ≥ 5** must be satisfied.

## Bibliography / references named by the official materials

- Wenliang Du, *Computer Security: A Hands-on Approach*, 2022.
- Ulfar Erlingsson, Yves Younan, Frank Piessens, *Low-Level Software Security by Example*, Springer, 2010.
- Justin Clarke, *SQL Injection Attacks and Defense*, 2nd ed., Elsevier, 2012.
- Dafydd Stuttard, Marcus Pinto, *The Web Application Hacker's Handbook*, 2nd ed., Wiley, 2011.
- Michael Howard, David LeBlanc, John Viega, *24 Deadly Sins of Software Security*, 2009.
- CWE Top 25 Most Dangerous Software Weaknesses.
- OWASP Top 10 Web Application Security Risks.
- CVE / MITRE vulnerability database.
- CERT Vulnerability Notes Database.

## Official sources

- Course page: https://edu.info.uaic.ro/securitate-software/
- Software Engineering programme sheet: https://edu.info.uaic.ro/fise-discipline/2025--2026/2024_Master_Ingineria%20sistemelor%20software_Software%20Engineering/ISS_sem_3_Fisa%20disciplinei_Securitate%20software.pdf
