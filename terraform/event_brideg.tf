
resource "aws_cloudwatch_event_rule" "lambda_pbl_regularly" {
  name = "lambda_pbl_regularly"
  schedule_expression = "cron(0 13-17 ? * 6 *)"
}

resource "aws_cloudwatch_event_target" "pbl" {
  arn  = aws_lambda_function.pbl.arn
  rule = aws_cloudwatch_event_rule.lambda_pbl_regularly.name
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.pbl.function_name
  principal     = "events.amazonaws.com"
}