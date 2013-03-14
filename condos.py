#!/usr/bin/env python

years_to_retirement = int(raw_input())
savings = float(raw_input())
percent_to_invest = float(raw_input())
income = []

for year in range(years_to_retirement):
    salary, bonus = raw_input().split()
    income.append((float(salary), float(bonus)))

property_tax = float(raw_input())
registration_fee = float(raw_input())
no_condos = int(raw_input())

condos = []

for condo in range(no_condos):
    condos.append(raw_input().split())

months = years_to_retirement * 12

