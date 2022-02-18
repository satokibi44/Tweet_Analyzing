
import sys
from main import main
def handler(event, context):
    main()
    return 'Hello from AWS Lambda using Python' + sys.version + '!'


if __name__ == "__main__":
    handler("aa", "bb")