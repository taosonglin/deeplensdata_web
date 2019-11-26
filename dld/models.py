# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cffex(models.Model):
    cffex_id = models.IntegerField(db_column='CFFEX_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ric_root = models.CharField(db_column='RIC Root', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    underlying_ric = models.CharField(db_column='Underlying RIC', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quote_permid = models.CharField(db_column='Quote PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type = models.CharField(db_column='Asset Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type_description = models.CharField(db_column='Asset Type Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype = models.CharField(db_column='Asset SubType', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype_description = models.CharField(db_column='Asset SubType Description', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_code = models.CharField(db_column='File Code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.DecimalField(db_column='Open', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    last = models.DecimalField(db_column='Last', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    universal_ask_price = models.DecimalField(db_column='Universal Ask Price', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    universal_bid_price = models.DecimalField(db_column='Universal Bid Price', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    universal_close_price = models.DecimalField(db_column='Universal Close Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    settlement_price = models.DecimalField(db_column='Settlement Price', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lot_size = models.DecimalField(db_column='Lot Size', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lot_units = models.CharField(db_column='Lot Units', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.DecimalField(db_column='Volume', max_digits=47, decimal_places=18, blank=True, null=True)  # Field name made lowercase.
    block_volume = models.DecimalField(db_column='Block Volume', max_digits=47, decimal_places=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    turnover = models.DecimalField(db_column='Turnover', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase.
    number_of_price_moves = models.DecimalField(db_column='Number of Price Moves', max_digits=47, decimal_places=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    implied_volatility = models.DecimalField(db_column='Implied Volatility', max_digits=34, decimal_places=11, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_trading_day = models.DateField(db_column='Last Trading Day', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    expiration_date = models.DateField(db_column='Expiration Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'CFFEX'


class Calendar(models.Model):
    date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendar'


class CapChange(models.Model):
    cap_change_id = models.IntegerField(db_column='Cap_Change_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_adjustment_factor = models.DecimalField(db_column='Actual Adjustment Factor', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_adjustment_type = models.CharField(db_column='Actual Adjustment Type', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_adjustment_type_description = models.CharField(db_column='Actual Adjustment Type Description', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    adjustment_factor = models.DecimalField(db_column='Adjustment Factor', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capital_change_ex_date = models.DateField(db_column='Capital Change Ex Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_marker = models.IntegerField(db_column='Delete Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    corporate_action_notes = models.CharField(db_column='Corporate Action Notes', max_length=4096, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Cap_Change'


class CapFactor(models.Model):
    ric = models.TextField(db_column='RIC', blank=True, null=True)  # Field name made lowercase.
    ticker = models.TextField(db_column='Ticker', blank=True, null=True)  # Field name made lowercase.
    actual_adjustment_type = models.TextField(db_column='Actual Adjustment Type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    actual_adjustment_factor = models.TextField(db_column='Actual Adjustment Factor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capital_change_ex_date = models.DateField(db_column='Capital Change Ex Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Cap_factor'


class Dividend(models.Model):
    dividend_id = models.IntegerField(db_column='Dividend_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_marker = models.IntegerField(db_column='Delete Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_announcement_date = models.DateField(db_column='Dividend Announcement Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_record_date = models.DateField(db_column='Dividend Record Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_ex_date = models.DateField(db_column='Dividend Ex Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_pay_date = models.DateField(db_column='Dividend Pay Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end_date = models.DateField(db_column='Period End Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_payment_type = models.CharField(db_column='Dividend Payment Type', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_frequency = models.BigIntegerField(db_column='Dividend Frequency', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_frequency_description = models.CharField(db_column='Dividend Frequency Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_length = models.BigIntegerField(db_column='Period Length', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_units = models.BigIntegerField(db_column='Period Units', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_units_description = models.CharField(db_column='Period Units Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_type_marker = models.BigIntegerField(db_column='Dividend Type Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_type_marker_description = models.CharField(db_column='Dividend Type Marker Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_rate = models.DecimalField(db_column='Dividend Rate', max_digits=18, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_currency = models.CharField(db_column='Dividend Currency', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_currency_description = models.CharField(db_column='Dividend Currency Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_source_of_funds = models.IntegerField(db_column='Dividend Source of Funds', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_source_of_funds_description = models.CharField(db_column='Dividend Source of Funds Description', max_length=16, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_tax_rate = models.DecimalField(db_column='Dividend Tax Rate', max_digits=18, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_tax_marker = models.BigIntegerField(db_column='Dividend Tax Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_tax_marker_description = models.CharField(db_column='Dividend Tax Marker Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dividend_market_event_id = models.BigIntegerField(db_column='Dividend Market Event ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    corporate_action_notes = models.CharField(db_column='Corporate Action Notes', max_length=4096, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_update_timestamp = models.CharField(db_column='Last Update Timestamp', max_length=24, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Dividend'


class Eps(models.Model):
    eps_id = models.IntegerField(db_column='EPS_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isin = models.CharField(db_column='ISIN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    gics_industry_code = models.CharField(db_column='GICS Industry Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_code_description = models.CharField(db_column='GICS Industry Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    earnings_announcement_date = models.DateField(db_column='Earnings Announcement Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_amount = models.DecimalField(db_column='EPS Amount', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_basis_number_of_shares = models.DecimalField(db_column='EPS Basis Number of Shares', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_calculation_basis = models.CharField(db_column='EPS Calculation Basis', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_currency = models.CharField(db_column='EPS Currency', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_general_marker = models.BigIntegerField(db_column='EPS General Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_general_marker_description = models.CharField(db_column='EPS General Marker Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_net_gross_marker = models.BigIntegerField(db_column='EPS Net/Gross Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eps_net_gross_marker_description = models.CharField(db_column='EPS Net/Gross Marker Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_end_date = models.DateField(db_column='Period End Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_length = models.BigIntegerField(db_column='Period Length', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_units = models.BigIntegerField(db_column='Period Units', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    period_units_description = models.CharField(db_column='Period Units Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_update_timestamp = models.CharField(db_column='Last Update Timestamp', max_length=24, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_marker = models.IntegerField(db_column='Delete Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'EPS'


class IndexEod(models.Model):
    index_eod_id = models.IntegerField(db_column='INDEX_EOD_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quote_permid = models.CharField(db_column='Quote PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issue_permid = models.CharField(db_column='Issue PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_name = models.CharField(db_column='Issuer Name', max_length=110, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_permid = models.CharField(db_column='Issuer PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_orgid = models.CharField(db_column='Issuer OrgID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type = models.CharField(db_column='Asset Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type_description = models.CharField(db_column='Asset Type Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype = models.CharField(db_column='Asset SubType', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype_description = models.CharField(db_column='Asset SubType Description', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_code = models.CharField(db_column='File Code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.DecimalField(db_column='Open', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    last = models.DecimalField(db_column='Last', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    universal_close_price = models.DecimalField(db_column='Universal Close Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'INDEX_EOD'


class OrderRecord(models.Model):
    order_record_id = models.IntegerField(db_column='Order_record_ID', primary_key=True)  # Field name made lowercase.
    dl_fund_code = models.CharField(db_column='DL Fund Code', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    system_time_stamp = models.CharField(db_column='System time stamp', max_length=24, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_id = models.BigIntegerField(db_column='Order ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bid_or_ask = models.IntegerField(db_column='BID or ASK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description_of_the_equity_instrument = models.CharField(db_column='Description of the equity instrument', max_length=34, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bid_or_ask_size = models.DecimalField(db_column='Bid or Ask Size', max_digits=27, decimal_places=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_volume = models.DecimalField(db_column='Trade Volume', max_digits=22, decimal_places=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    turnover = models.DecimalField(db_column='Turnover', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Order_record'


class Ref(models.Model):
    ref_id = models.IntegerField(db_column='REF_ID', primary_key=True)  # Field name made lowercase.
    file_code = models.CharField(db_column='File Code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dlc_root = models.CharField(db_column='DLC Root', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    trading_symbol = models.CharField(db_column='Trading Symbol', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    china_connect_eligibility_indicator_code = models.CharField(db_column='China Connect Eligibility Indicator Code', max_length=9, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    china_connect_eligibility_indicator_description = models.CharField(db_column='China Connect Eligibility Indicator Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isin = models.CharField(db_column='ISIN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    sedol = models.CharField(db_column='SEDOL', max_length=7, blank=True, null=True)  # Field name made lowercase.
    cusip = models.CharField(db_column='CUSIP', max_length=9, blank=True, null=True)  # Field name made lowercase.
    is_primary_issue_flag = models.CharField(db_column='Is Primary Issue Flag', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_orgid = models.CharField(db_column='Issuer OrgID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    company_name = models.CharField(db_column='Company Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    underlying_ric = models.CharField(db_column='Underlying RIC', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    underlying_security_description = models.CharField(db_column='Underlying Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    share_class = models.CharField(db_column='Share Class', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suspend_flag = models.CharField(db_column='Suspend Flag', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tick_size = models.BigIntegerField(db_column='Tick Size', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tick_size_currency_code = models.CharField(db_column='Tick Size Currency Code', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tick_size_currency_description = models.CharField(db_column='Tick Size Currency Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    market_mic = models.CharField(db_column='Market MIC', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    market_segment_mic = models.CharField(db_column='Market Segment MIC', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_code = models.CharField(db_column='GICS Industry Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_code_description = models.CharField(db_column='GICS Industry Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_description_code = models.CharField(db_column='GICS Industry Description Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_description_code_description = models.CharField(db_column='GICS Industry Description Code Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_group_code = models.CharField(db_column='GICS Industry Group Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_group_code_description = models.CharField(db_column='GICS Industry Group Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_sector_code = models.CharField(db_column='GICS Sector Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_sector_code_description = models.CharField(db_column='GICS Sector Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organizational_subtype_code = models.CharField(db_column='Organizational SubType Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organizational_subtype_description = models.CharField(db_column='Organizational SubType Description', max_length=57, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organizational_type_code = models.CharField(db_column='Organizational Type Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organizational_type_description = models.CharField(db_column='Organizational Type Description', max_length=33, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    foreign_ownership_percent_of_limit = models.BigIntegerField(db_column='Foreign Ownership Percent of Limit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    foreign_ownership_percent_of_total_shares = models.BigIntegerField(db_column='Foreign Ownership Percent of Total Shares', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    foreign_ownership_shares_allowed = models.BigIntegerField(db_column='Foreign Ownership Shares Allowed', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    foreign_ownership_shares_held = models.BigIntegerField(db_column='Foreign Ownership Shares Held', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    foreign_ownership_shares_remaining = models.BigIntegerField(db_column='Foreign Ownership Shares Remaining', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'REF'


class Shibor(models.Model):
    shibor_id = models.IntegerField(db_column='SHIBOR_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type = models.CharField(db_column='Asset Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type_description = models.CharField(db_column='Asset Type Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype = models.CharField(db_column='Asset SubType', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype_description = models.CharField(db_column='Asset SubType Description', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.DecimalField(db_column='Open', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    last = models.DecimalField(db_column='Last', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    universal_ask_price = models.DecimalField(db_column='Universal Ask Price', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    universal_bid_price = models.DecimalField(db_column='Universal Bid Price', max_digits=36, decimal_places=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    universal_close_price = models.DecimalField(db_column='Universal Close Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SHIBOR'


class ShseEqEod(models.Model):
    sse_eq_eod_id = models.IntegerField(db_column='SSE_EQ_EOD_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quote_permid = models.CharField(db_column='Quote PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issue_permid = models.CharField(db_column='Issue PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_name = models.CharField(db_column='Issuer Name', max_length=110, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_permid = models.CharField(db_column='Issuer PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_orgid = models.CharField(db_column='Issuer OrgID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type = models.CharField(db_column='Asset Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type_description = models.CharField(db_column='Asset Type Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype = models.CharField(db_column='Asset SubType', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype_description = models.CharField(db_column='Asset SubType Description', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_code = models.CharField(db_column='File Code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.DecimalField(db_column='Open', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    last = models.DecimalField(db_column='Last', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    universal_close_price = models.DecimalField(db_column='Universal Close Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SHSE_EQ_EOD'


class SzseEqEod(models.Model):
    szse_eq_eod_id = models.IntegerField(db_column='SZSE_EQ_EOD_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quote_permid = models.CharField(db_column='Quote PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    issue_permid = models.CharField(db_column='Issue PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_name = models.CharField(db_column='Issuer Name', max_length=110, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_permid = models.CharField(db_column='Issuer PermID', max_length=18, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    issuer_orgid = models.CharField(db_column='Issuer OrgID', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trading_status = models.IntegerField(db_column='Trading Status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status = models.CharField(db_column='Asset Status', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_status_description = models.CharField(db_column='Asset Status Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type = models.CharField(db_column='Asset Type', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_type_description = models.CharField(db_column='Asset Type Description', max_length=30, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype = models.CharField(db_column='Asset SubType', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    asset_subtype_description = models.CharField(db_column='Asset SubType Description', max_length=20, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code = models.CharField(db_column='Currency Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    currency_code_description = models.CharField(db_column='Currency Code Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    file_code = models.CharField(db_column='File Code', max_length=15, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    open = models.DecimalField(db_column='Open', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    high = models.DecimalField(db_column='High', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    low = models.DecimalField(db_column='Low', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    last = models.DecimalField(db_column='Last', max_digits=18, decimal_places=9, blank=True, null=True)  # Field name made lowercase.
    universal_close_price = models.DecimalField(db_column='Universal Close Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    volume = models.BigIntegerField(db_column='Volume', blank=True, null=True)  # Field name made lowercase.
    turnover = models.DecimalField(db_column='Turnover', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'SZSE_EQ_EOD'


class ShseIndex(models.Model):
    ticker = models.TextField(db_column='Ticker', blank=True, null=True)  # Field name made lowercase.
    universal_close_price = models.TextField(db_column='Universal Close Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rate = models.TextField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shse_index'


class ShseIndexWeekly(models.Model):
    week = models.BigIntegerField(db_column='Week', blank=True, null=True)  # Field name made lowercase.
    rate = models.TextField(db_column='Rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shse_index_weekly'


class Tso(models.Model):
    tso_id = models.IntegerField(db_column='TSO_ID', primary_key=True)  # Field name made lowercase.
    dlc = models.CharField(db_column='DLC', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    security_description = models.CharField(db_column='Security Description', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=3, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    isin = models.CharField(db_column='ISIN', max_length=12, blank=True, null=True)  # Field name made lowercase.
    shares_amount = models.BigIntegerField(db_column='Shares Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shares_amount_date = models.DateField(db_column='Shares Amount Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shares_amount_type = models.CharField(db_column='Shares Amount Type', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shares_amount_type_description = models.CharField(db_column='Shares Amount Type Description', max_length=40, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shares_amount_type_default_flag = models.CharField(db_column='Shares Amount Type Default Flag', max_length=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trbc_business_sector_code = models.CharField(db_column='TRBC Business Sector Code', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trbc_business_sector_code_description = models.CharField(db_column='TRBC Business Sector Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trbc_industry_code = models.CharField(db_column='TRBC Industry Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trbc_industry_code_description = models.CharField(db_column='TRBC Industry Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_code = models.CharField(db_column='GICS Industry Code', max_length=8, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gics_industry_code_description = models.CharField(db_column='GICS Industry Code Description', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    market_mic = models.CharField(db_column='Market MIC', max_length=4, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_update_timestamp = models.CharField(db_column='Last Update Timestamp', max_length=24, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    delete_marker = models.IntegerField(db_column='Delete Marker', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'TSO'


class TradeDate(models.Model):
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Trade_date'


class TradeRecord(models.Model):
    trade_record_id = models.IntegerField(db_column='Trade_record_ID', primary_key=True)  # Field name made lowercase.
    dl_fund_code = models.CharField(db_column='DL Fund Code', max_length=12, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.DateField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_time = models.BigIntegerField(db_column='Trade Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_id = models.BigIntegerField(db_column='Order ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.CharField(db_column='Ticker', max_length=50, blank=True, null=True)  # Field name made lowercase.
    description_of_the_equity_instrument = models.CharField(db_column='Description of the equity instrument', max_length=34, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bid_or_ask = models.IntegerField(db_column='BID or ASK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_volume = models.DecimalField(db_column='Trade Volume', max_digits=22, decimal_places=7, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_price = models.DecimalField(db_column='Trade Price', max_digits=39, decimal_places=14, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.CharField(db_column='Exchange Code', max_length=6, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.CharField(db_column='Exchange Description', max_length=70, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Trade_record'


class TradeRecordAdjusted(models.Model):
    dl_fund_code = models.TextField(db_column='DL Fund Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_date = models.TextField(db_column='Trade Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_time = models.TextField(db_column='Trade Time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    order_id = models.TextField(db_column='Order ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ticker = models.TextField(db_column='Ticker', blank=True, null=True)  # Field name made lowercase.
    description_of_the_equity_instrument = models.TextField(db_column='Description of the equity instrument', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bid_or_ask = models.TextField(db_column='BID or ASK', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_volume = models.TextField(db_column='Trade Volume', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trade_price = models.TextField(db_column='Trade Price', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_code = models.TextField(db_column='Exchange Code', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    exchange_description = models.TextField(db_column='Exchange Description', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    num_forward = models.TextField(db_column='Num_forward', blank=True, null=True)  # Field name made lowercase.
    trade_price_forward = models.TextField(db_column='Trade_price_forward', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trade_record_adjusted'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, blank=True, null=True)
    passwd = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
