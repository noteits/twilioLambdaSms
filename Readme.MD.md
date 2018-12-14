#Create and Install Twilio Lambda function to send sms on macos
`curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`
   
`python get-pip.py` 
   
`sudo python get-pip.py`

`pip2 install twilio==5.5.0 -t .`
   
`git clone https://github.com/noteits/twilioLambdaSms.git` 
  
`zip -r twilioLambda.zip *`

**Upload zip arcive to lambda function and run test execution** 

{   
  "to_number": "+00000000000",    
  "from_number": "+11111111111",    
  "message": "hello from API"    
}    

where to is your authorized number and from your number provided by twilio.

