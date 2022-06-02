# Five Stages Of Pentesting

To day we talk about the five stages of pentesting 
But first you need to know this 

# What is Cybersecurity?

Cybersecurity is one of the hottest fields to be in, thanks to so many companies going remote. Cyber threats are increasing and cybercriminals are finding new ways to exploit systems.

Penetration testing is how ethical hackers work. They think like bad hackers and attack their own systems. This helps them understand their strengths and weaknesses and protect their organizational assets.

A pen-test is comprised of multiple stages. You cannot simply get into a system by using a tool unless the target is hopelessly vulnerable.

In the most cases the system may be protected by  an anti-virus of a firewall and you need the skills to pass it 

So lets back to our subject The Five Stages the first one is :

# Reconnaissance

This is the most important stage here were you will collect information about the target 

And the more information you get it become easier for you to get into the system 

And you can do it by using a tools like (Maltego) (Theharvester) (GHDB : Google Hacks Database) (Sherlock) (PhoneInfoGa) (SpiderFoot)


# Scanning

This is the part where you come in contact with the target. 

Scanning involves sending packets of data to the target and interpreting their response.

Its very usefull its give you knowlodge about the target IP Adress Open-Ports and OS Information and the service that installed on the system .

And you can do it by using (Nmap is the Best) (Netdiscover for local enumration) (Recon-ng) (Nessus One Of The best)

# Exploitation
This is the part where you gain access to the system.

A successful exploit should give you control of the system to at least a user level.

From there you perform privilege escalation to gain root access to the target.

And you can do it by using (Metasploit Framework) (SQLMap For SQL Injection) (Armitage GUI Metasploit)

# Maintaining Access
Gaining access to systems is not easy, especially on corporate networks. After all the hard work you have done to exploit a system, it won't make sense to go through the same process to exploit the target again.

This is where maintaining access comes in. You can install backdoors, keyloggers, and other pieces of code that let you into the system whenever you want.

Metasploit gives you tools like keyloggers and Meterpreter backdoors to maintain access to an exploited system. You can also install custom Rootkits or Trojans after gaining access.

A rootkit is a piece of code that lets the attacker have admin access to the system it is attached to. Rootkits can also be installed when you download files from malicious websites.

Trojan horses are software that looks like useful software (for example, adobe photoshop) but can contain a hidden piece of malicious software. This is common among pirated software where attackers embed trojans within popular software like MS Office.

# Reporting 
Reporting is the final part of a penetration test. It is what differentiates between an attacker and an ethical hacker.

Once your penetration test is complete, you summarize all the steps you have taken from recon to gaining access. This will help the organization to understand its security architecture and defend itself better.

A report is also useful when you are working as a team. You will not be able to conduct a penetration test for a large organization alone. Reports also make the client understand the efforts of the team and help justify the compensation.