import sys

# Pitanje 1: Šta se dešava ako igrač unese prazan niz za poruku?
# Odgovor: Ako igrač unese prazan niz, program se odmah prekida zbog `sys.exit()`
# i ništa se neće ispisati na ekranu.
#
# Pitanje 2: Je li važno koji su znakovi koji nisu razmak u nizu `bitmap` varijable?
# Odgovor: Nije važno koji su tačno znakovi sve dok nisu razmak. Program samo
# provjerava da li je znak razmak ili nije, a na svim ostalim mjestima ispisuje
# slova iz poruke.
#
# Pitanje 3: Šta predstavlja varijabla `i` stvorena u retku 37?
# Odgovor: Varijabla `i` predstavlja poziciju, odnosno indeks trenutnog znaka u
# jednom redu. Pomoću nje program zna koje slovo iz poruke treba ispisati.
#
# Pitanje 4: Koja se greška događa ako izbrišete ili komentirate `print()` u retku 44?
# Odgovor: Neće se pojaviti klasična greška u programu, ali će ispis biti loš.
# Redovi se neće prelamati, pa će cijela slika izaći u jednom dugom redu.

# (!) Try changing this multiline string to any image you like:
# There are 68 periods along the top and bottom of this string:

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print('Enter the message to display with the bitmap.')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Print an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    print()  # Print a newline.
