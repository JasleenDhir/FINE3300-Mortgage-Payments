# FINE 3300 Assigment 1, Manahil Waraich & Jasleen Dhir
'''The primary goal of designing this code is to help users understand
the differences in payment frequencies for fixed-rate mortgages. This applies
both to first-time home buyers and to those whose mortgages are up for renewal.
The main users of this code are potential and current homeowners or financial
planners.'''

class Mortgage:
    # Prompt the user for the principal amount of the mortgage
    principal = float(input('What is the principal amount of your mortgage? '))
    # Prompt the user for the interest rate and convert from percentage to a decimal
    rate = float(input('What is your quoted interest rate as a percentage? ')) / 100
    # Prompt the user for the amortization period in years
    amortization = int(input('What is the amortization period of your mortgage in years? '))

    # Calculate the number of payment periods
    def mortgage_payments(principal, rate, amortization):
        "Calculate different types of mortgage payments."
        n_months = amortization * 12
        n_semi_monthly = amortization * 24
        n_bi_weekly = amortization * 26
        n_weekly = amortization * 52

        # Calculate the present value of an annuity factor
        def present_value_annuity(r, n):
            "Calculate the present value of an annuity factor."
            return (1 - (1 + r) ** -n) / r

        # Convert the quoted semiannual rate to a periodic rate
        def calculate_periodic_rate(quoted_rate, periods_per_year):
            "Convert the quoted semiannual rate to a periodic rate."
            rq = quoted_rate  # already converted to decimal earlier
            return ((1 + rq / 2) ** (2 / periods_per_year)) - 1

        # Calculate rates for different payment frequencies
        monthly_rate = calculate_periodic_rate(rate, 12)
        semi_monthly_rate = calculate_periodic_rate(rate, 24)
        bi_weekly_rate = calculate_periodic_rate(rate, 26)
        weekly_rate = calculate_periodic_rate(rate, 52)

        # Calculate present value annuities for different payment frequencies
        pva_monthly = present_value_annuity(monthly_rate, n_months)
        pva_semi_monthly = present_value_annuity(semi_monthly_rate, n_semi_monthly)
        pva_bi_weekly = present_value_annuity(bi_weekly_rate, n_bi_weekly)
        pva_weekly = present_value_annuity(weekly_rate, n_weekly)

        # Calculate payments for each frequency
        monthly_payment = principal / pva_monthly
        semi_monthly_payment = principal / pva_semi_monthly
        bi_weekly_payment = principal / pva_bi_weekly
        weekly_payment = principal / pva_weekly
        rapid_bi_weekly_payment = monthly_payment / 2
        rapid_weekly_payment = monthly_payment / 4

        # Output the calculated payment amounts formatted to two decimal places
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Semi-monthly Payment: ${semi_monthly_payment:.2f}")
        print(f"Bi-weekly Payment: ${bi_weekly_payment:.2f}")
        print(f"Weekly Payment: ${weekly_payment:.2f}")
        print(f"Rapid Bi-weekly Payment: ${rapid_bi_weekly_payment:.2f}")
        print(f"Rapid Weekly Payment: ${rapid_weekly_payment:.2f}")

# Call the method with the appropriate variables
Mortgage.mortgage_payments(Mortgage.principal, Mortgage.rate, Mortgage.amortization)