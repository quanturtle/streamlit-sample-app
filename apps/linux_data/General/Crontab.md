```
# every minute
* * * * * <command> >/dev/null 2>&1

# every hour
0 * * * * <command> >/dev/null 2>&1

# every day (at midnight)
0 0 * * * <command> >/dev/null 2>&1

# every month (at midnight on day-of-month 1)
0 0 1 * * <command> >/dev/null 2>&1

# every year (at midnight on day-of-month 1 in January)
0 0 1 1 * <command> >/dev/null 2>&1
```
