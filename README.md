# ***randstr***

    A Small Python package for generating strings with random characters built on top of the random module.

## ***Module rs***

<table width="100%">
	<tr>
		<th align="left">
            Method
        </th>
		<th align="left">
            Description
        </th>
	</tr>
	<tr>
		<td>
            <code>randdigit()</code>
        </td>
		<td>
            Generates a random digit ranging from 0 to 9 (Digits in Decimal Number System) and returns it as a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>randalpha()</code>
        </td>
		<td>
            Generates a random lowercase letter from the english alphabet and returns it as a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>randspec()</code>
        </td>
		<td>
            Generates a random special character and returns it as a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>randstr(string_length, seed_type)</code>
        </td>
		<td>
            Return a string with random values of designated int length (Cap of 10000).
            The random value combos are selected by using a specific string for the seed_type argument. <br/>
            The seed_type argument value options (not case sensitive) are as follows: <br/>
                "al" - (Alphabet Lower) Random lowercase alphabet letters. <br/>
                "au" - (Alphabet Upper) Random uppercase alphabet letters. <br/>    
                "dig" - (Digit) Random digits 0-9. <br/>
                "spec" - (Special) Random special characters. <br/>
                "ad" - (Alphabet Lower | Alphabet Upper | Digit) Random lowercase & uppercase alphabet letters. Random digits 0-9. <br/>
                "ads" - (Alphabet Lower | Alphabet Upper | Digit | Special) Random lowercase & uppercase alphabet letters. Random digits 0-9. Random special characters.
        </td>
	</tr>
</table>

[Back to Top](#randstr)

---
