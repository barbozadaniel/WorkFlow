import SendEmail
import DocChrome
import string

def ParseAndPerform(commands):
    for command in commands:
        if(command[:4].upper() == 'OPEN'):
            url_temp = command[5:].lower();
            url = 'www.'+ url_temp +'.com';
            print('Opening.. ' + url);
            #print('\n');
            DocChrome.open_chrome(url);
            
        elif(command[:4].upper() == 'SEND'):
            message_temp = command[5:];
            message_temp = message_temp[::-1];

            name = message_temp.split(' ')[0].strip()[::-1];
        
            pos = 0;
            count = 2;
            for char in message_temp:
                if char == ' ':
                    count = count - 1
                    if(count == 0):
                        break;
                pos = pos + 1

            message = message_temp[pos+1:][::-1];
            SendEmail.email_google(name, message);

            print('"' + message + '" sent to ' + name);
            #print('\n');
            
        elif(command[:5].upper() == 'WRITE'):
            doc_temp = command[6:];
            DocChrome.add_to_doc(doc_temp);
            print('"' + doc_temp + '" written into the Document');
            #print('\n');
            
        
