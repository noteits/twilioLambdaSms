**Create and Install Twilio Lambda function to send sms on macos**
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
   
`python get-pip.py` 
   
`sudo python get-pip.py`

`git clone https://github.com/noteits/twilioLambdaSms.git`

`cd twilioLambdaSms`

`pip2 install twilio==5.5.0 -t .`

**Change account sid and token in function or pass it as a variables, then:**

   
`zip -r twilioLambda.zip *`

**Upload zip arcive to lambda function and run test execution** 

{   
  "to_number": "+00000000000",    
  "from_number": "+11111111111",    
  "message": "hello from API"    
}    

where to is your authorized number and from your number provided by twilio.


 [reference](https://www.twilio.com/blog/2017/06/build-serverless-api-amazon-web-services-api-gateway.html)
