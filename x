There have been several Python programs failing after the SQR-to-Python roll-out. Root cause is that the code doesn't gracefully handle null Client Payroll Numbers, which can sometimes exist in BENDB.

Pet Matt Ebbecke, in order to prevent future Python programs/reports from failing, we need to implement the following code change: nvl the cli_pr_client_nbr to '00000000'.



