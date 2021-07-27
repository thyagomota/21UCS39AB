# CS39AB - Cloud Computing - Summer 2021
# Instructor: Thyago Mota
# Description: Activity 26 - Greetings Lambda Function

from string import Template

HTML_TEMPLATE = \
'''
    <!DOCTYPE html>
        <html>
            <head>
                <style>
                    h1 {
                        color: blue;
                        font-family: verdana;
                        font-size: 300%;
                    }
                    p  {
                        color: red;
                        font-family: courier;
                        font-size: 160%;
                    }
                </style>
            </head>
            <body>
                <h1>Hello $name!</h1>
                <p>I hope you are enjoying learning about lambda functions.</p>
            </body>
        </html>
'''

def lambda_handler(event, context):
    if 'queryStringParameters' in event and 'name' in event['queryStringParameters']: 
        name = event['queryStringParameters']['name']
        html = Template(HTML_TEMPLATE).safe_substitute(name=name)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html'
            },
            'body': html
        }
    else:
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html'
            },
            'body': 'You need to provide a name!'
        }

