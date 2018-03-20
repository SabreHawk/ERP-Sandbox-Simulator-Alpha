using System;
using System.Collections;

namespace MessageManager {
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Hello World!");
            ArrayList tmp_a = new ArrayList();
            tmp_a.Add(2);
            tmp_a.Add("22");
            for (int i = 0; i < tmp_a.Count; ++i) {
                Console.WriteLine(tmp_a[i]);
            }
            Console.ReadKey();
        }
    }
}
