using System.Collections.Generic;
using System;
using System.Diagnostics;

namespace Lab4
{
    public class Program
    {
        static void Main()
        {
            Stopwatch time_count = new Stopwatch();
            var files = new List<string> {
             "www.columbia.edu/~fdc/sample.html#effects",
             "www.columbia.edu/~fdc/sample.html#lists"
        };

            Console.WriteLine("1.Directly implementing the parser on the callbacks (event-driven).");
            time_count.Start();
            DirectCallbackImplementation.Run(files);
            time_count.Stop();
            TimeSpan timefirstimplementation = time_count.Elapsed;

            Console.WriteLine("\n\n\n\n\n\n\n");
            Console.WriteLine("2.Wraping the connect/send/receive operations in tasks");
            time_count.Restart();
            WrapOperationsInTaskImplementation.Run(files);
            time_count.Stop();
            TimeSpan timesecondimplementation = time_count.Elapsed;

            Console.WriteLine("\n\n\n\n\n\n\n");
            Console.WriteLine("3. Using the async/await mechanism.");
            time_count.Restart();
            AsyncAwaitMechanismImplementation.Run(files);
            time_count.Stop();
            TimeSpan timethirdimplementation = time_count.Elapsed;

            Console.WriteLine("\n\n\n\n\n\n\n");
            Console.WriteLine("Time for each implementation:");
            Console.WriteLine("Direct callback: {0}", timefirstimplementation);
            Console.WriteLine("Wrap operations in tasks: {0}", timesecondimplementation);
            Console.WriteLine("Async await mechanism: {0}", timethirdimplementation);
        }
    }
}