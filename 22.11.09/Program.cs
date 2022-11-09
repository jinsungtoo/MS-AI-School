using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Mail;
using System.Text;
using System.Threading.Tasks;

using System.Timers;
using Microsoft.Azure.Devices.Client; 
using Newtonsoft;

namespace IoTClient
{
    internal class Program
    {
        private static System.Timers.Timer SensorTimer;
        private const string DeviceConnectionString = "본인의 ID ";
        private const string DeviceID = "device1"; 
        private static DeviceClient SensorDevice = null;

        private static DummySensor DummySensor = new DummySensor();  
        static void Main(string[] args)
        {
            SetTimer();

            SensorDevice = DeviceClient.CreateFromConnectionString(DeviceConnectionString, DeviceID);
            
            if(SensorDevice == null)
            {
                Console.WriteLine("Failed to create DeviceClient !!");
                SensorTimer.Stop();
            }

            Console.WriteLine("\nPress Enter Key to exit the application...\n");
            Console.WriteLine("The application started at {0:HH:mm:ss.fff}", DateTime.Now );
            Console.ReadLine();
            SensorTimer.Stop();
            SensorTimer.Dispose();
        }

        private static void SetTimer() // Timer: 2초에 한번씩 
        {
            SensorTimer = new System.Timers.Timer(2000);
            SensorTimer.Elapsed += SensorTimer_Elapsed;
            SensorTimer.AutoReset = true;
            SensorTimer.Enabled = true;
        }

        private static async void SensorTimer_Elapsed(object sender, ElapsedEventArgs e)
        {
            Console.WriteLine("The Elapshed event was raised at {0:HH:mm:ss.fff}", e.SignalTime );

            // Process 보다 작은 단위 Thread (Process > Thread)
            await SendEvent();
            await ReceiveCommands();
        }

        
        private static async Task SendEvent() 
        {
            WeatherModel model = DummySensor.GetWeatherModel(DeviceID);  

            
            string json = Newtonsoft.Json.JsonConvert.SerializeObject(model);

            Console.WriteLine(json);

            Message message = new Message(Encoding.UTF8.GetBytes(json));  // Encoding
            await SensorDevice.SendEventAsync(message); 
        }

        private static async Task ReceiveCommands()  // Cloud에서 Device로 message send
        {
            Message receivedMessage;
            string messageData;

            receivedMessage = await SensorDevice.ReceiveAsync(TimeSpan.FromSeconds(1));  // receive message

            if (receivedMessage != null)
            {
                messageData = Encoding.ASCII.GetString(receivedMessage.GetBytes());  // Encoding
                Console.WriteLine("\t{0}> Received message: {1}", DateTime.Now.ToLocalTime(), messageData);

                await SensorDevice.CompleteAsync(receivedMessage);
            }
        }


    }
}
