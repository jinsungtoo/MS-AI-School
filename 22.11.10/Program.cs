using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Data.SqlClient;
using System.Data;

namespace CRUD_Sample1
{
    internal class Program
    { //멤버변수
        private const string ConnectionString = "Server=tcp:labuser16sqlserver2.database.windows.net,1433;Initial Catalog=labuser16sql2;Persist Security Info=False;User ID=winkey;Password=c10b06!!!!!!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";

        static void Main(string[] args)
        { //지역변수
            SqlConnection con = new SqlConnection(ConnectionString); //새 커넥션 개체 생성
            SqlCommand cmd = con.CreateCommand();
            IDataReader reader = null;

            string query = "SELECT * FROM production.brands WHERE brand_id > @id";
            cmd.CommandText = query;
            cmd.Parameters.Add(new SqlParameter("@id", SqlDbType.Int)).Value = 5;

            con.Open();
            Console.WriteLine("Database Connected!");
            reader = cmd.ExecuteReader(); //실행결과가 reader 객체로 떨어짐

            while(reader.Read()) // reader안에 있는 객체를 읽어들임
            {
                Console.WriteLine("{0} -{1}", reader.GetInt32(0), reader.GetString(1));
            }

            con.Close();

            Console.ReadLine(); // 콘솔을 닫지 않고 계속 멈추게 해줌
        }
    }
}
