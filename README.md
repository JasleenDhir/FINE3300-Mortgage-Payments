## FINE 3300 Assignment 1, Manahil Waraich & Jasleen Dhir

Link to GitHub Manahil: https://github.com/ManahilW/FINE3300-Mortgage-Payments <br>
Link to GitHub Jasleen: https://github.com/JasleenDhir/FINE3300-Mortgage-Payments

The primary goal of designing this code is to help users understand the differences in payment frequencies for fixed-rate mortgages. This applies both to first-time home buyers and to those whose mortgages are up for renewal. The main users of this code are potential and current homeowners or financial planners.

This Mortgage Calculator program is implemented through a Python class named “Mortgage”. It engages users by prompting them to provide key financial figures: the principal amount of the mortgage, the annual interest rate, and the length of time over which the loan is to be amortized. These inputs are critical for determining the monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, and rapid weekly mortgage payments.

**Functionality Overview:**
1. The first step involves gathering the user’s inputs:
- Principal: The original total amount of the loan.
- Interest Rate: The annual interest rate, converted from a percentage to a decimal for calculation purposes.
- Amortization Period: The total period over which the loan amount is to be paid off, expressed in years.

2. The second step involves, the conversion of annual interest rates to periodic rates:
- This conversion accounts for semi-annual compounding, which is a standard in many financial contexts.
- Periodic rates are calculated separately for monthly, semi-monthly, bi-weekly, and weekly payment plans.
- The formula used, *((1 + r / 2) ** (2 / n) - 1)*, adjusts the annual rate to reflect the compounding effect over the specified number of periods per year.

3. Next is the calculation of present value annuities for each payment frequency:
- Utilizes the present value annuity formula: *(1 - (1 + r) ** -n) / r*
- This formula helps to determine the total amount payable per period by considering the time value of money.

4. Then determining the mortgage payments for each schedule:
- Each payment type (monthly, semi-monthly, etc.) is calculated by dividing the principal by the corresponding annuity factor derived from the present value calculations.
- This results in the exact periodic payment amount required to fully amortize the loan over the specified period.

5. Lastly, formatting and output:
- The calculated payments are formatted to two decimal places for clarity and precision
- Payments are printed to the frequency payment for each type, including rapid options which simply halve or quarter the regular monthly payment, allowing for faster amortization of the loan.

The Mortgage class is designed to simulate real-world mortgage payment calculations that potential homeowners or financial planners might use to estimate periodic payments under different payment schedules. This simulation aids in understanding how changing payment frequencies impacts the amortization schedule and total interest paid.

The goal is to provide users with clear and precise payment breakdowns under various common payment schedules, enabling better financial planning and understanding of mortgage amortization impacts. To run, the user will be prompted to enter the principal, rate, and amortization period directly into the console. The output will display the calculated payments for each of the mentioned schedules.

For example, if the user were to input *a principal amount of $500,000, quoted at 5.5%, and
amortized over 25 years* the output would be as follows:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Monthly Payment: $3051.96 <br>
&nbsp;&nbsp;&nbsp;&nbsp;Semi-monthly Payment: $1524.25<br>
&nbsp;&nbsp;&nbsp;&nbsp;Bi-weekly Payment: $1406.88<br>
&nbsp;&nbsp;&nbsp;&nbsp;Weekly Payment: $703.07<br>
&nbsp;&nbsp;&nbsp;&nbsp;Rapid Bi-weekly Payment: $1525.98<br>
&nbsp;&nbsp;&nbsp;&nbsp;Rapid Weekly Payment: $762.99<br>