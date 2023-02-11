"""
Given an input in string form of "01-10-2018" convert that into "January 10th" form.
Make sure you add the "th", 'rd' etc at the end. Both outputs must be string.
"""

def date_str_format(sdate: str) -> str:
    month_dict = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    day_dict = {
        '1': '1st',
        '2': '2nd',
        '3': '3rd'
    }
    s_month, s_day = sdate.split('-')[:2]
    if s_day[-1] in day_dict.keys():
        tmp_day_str = day_dict[s_day[-1]]
    else:
        tmp_day_str = s_day[-1] + 'th'

    if len(s_day) > 1:
        tmp_day_str = s_day[0] + tmp_day_str
    return month_dict[s_month] + ' ' + tmp_day_str


print(date_str_format('06-18-2018'))