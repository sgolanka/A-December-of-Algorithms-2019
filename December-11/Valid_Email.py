"""
Now, for today's challenge implement your own email address verification algorithm.
For the sake of simplicity, assume that a valid email address has the following format:
local_part@domain
The local_part should contain only alphabets, numbers and the characters: _, ., -.
The domain should contain only alphabets followed by .com
"""


def is_valid_email(email_address):
    """
    Given a possible email address, determine if it is valid.

    :param email_address: a string with a proposed email address
    :return: true if email_address is valid, false if not

    """

    valid = False

    if '@' in email_address and '.' in email_address:  # check for the basic elements
        
        # allowable domains
        email_end = ('com', 'org', 'edu', 'net', 'mail', 'me')
        end_part = email_address[-3:]

        if end_part in email_end:  # look at characters in local_part if proper ending
            local_part = email_address[:email_address.index('@')]
            valid = True

            l_p_chars = 'abcdefghijklmnopqrstuvwxyz'
            # allowable characters for the domain
            dom_chars = l_p_chars + l_p_chars.upper()
            # allowable characters for the local part
            l_p_chars += l_p_chars.upper() + '_-.123456789'

            for ch in local_part:
                if ch not in l_p_chars:
                    valid = False
                    break

            if valid:  # look at characters in domain
                domain_part = email_address[email_address.index('@') + 1:len(email_address) - 4]
                for ch in domain_part:
                    if ch not in dom_chars:
                        valid = False
                        break

    return valid


attempted_addresses = ("yoyo@fff.com", 'hey_now!@trevor.org', 'sgolanka@trevor.org', 'smg2141@tc.edu', 'abc@123.com.',
                       'SAM_ADAMS@beer.net', 'h#ck_with_you@fleen.com', 'wh@t@who.org')

for attempted_address in attempted_addresses:
    if is_valid_email(attempted_address):
        print('{} is a valid email address.'.format(attempted_address))
    else:
        print('{} is NOT a valid email address.'.format(attempted_address))
