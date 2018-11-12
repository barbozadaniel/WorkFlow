import ParseText;
import CaptureAndDetect;

def main():
    commands = CaptureAndDetect.GetCommands();
    print('Detected Commands:');
    print('------------------');
    print(commands);
    print('\n');
    print('Output Tasks:');
    print('------------------');
    ParseText.ParseAndPerform(commands);

if __name__ == "__main__":
    main()
