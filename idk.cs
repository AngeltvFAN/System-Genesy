using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace kaziks
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.Title = GenerateRandomName(40);
            Console.WriteLine("Ok, so, you got hacked by HydraX exploit, all your data will be erased from this device  and it will be send to a remote server that we can handle, just cry.");

                    //Btw, if you arent blind you can easily see that this is a JOKE, the script is just made to scare, it inst real.
            Console.ReadKey();
        }
        public static string GenerateRandomName(int length)
        {
            const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            Random random = new Random();
            StringBuilder result = new StringBuilder(length);
            for (int i = 0; i < length; i++)
            {result.Append(chars[random.Next(chars.Length)]);}
            return result.ToString();
        }
    }
}
