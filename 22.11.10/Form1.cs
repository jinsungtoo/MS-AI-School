using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

using System.Data.SqlClient;
using System.Collections;

namespace SQLServer01
{
    public partial class frmMain : Form
    {
        private const string CONNECTION_STRING = "Server=tcp:labuser16sqlserver2.database.windows.net,1433;Initial Catalog=labuser16sql2;Persist Security Info=False;User ID=winkey;Password=c10b06!!!!!!;MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;";
        private SqlConnection SqlCon = null;
        private SqlCommand SqlCmd = null;
        private SqlDataAdapter SqlApt = new SqlDataAdapter();

        private DataSet dataMain = new DataSet();

        public frmMain()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SqlCon = new SqlConnection(CONNECTION_STRING);
            button1.Enabled = false;
        }

        private void btnGetData_Click(object sender, EventArgs e)
        {
            string query = "SELECT * FROM production.brands";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.CommandText = query;

            SqlApt.SelectCommand = cmd;
            SqlApt.Fill(dataMain);

            lstBrends.Items.Clear();

            DataRowCollection dataRows = dataMain.Tables[0].Rows;

            for (int i = 0; i < dataRows.Count; i++)
            {
                lstBrends.Items.Add(dataRows[i][1].ToString());
            }



            btnGetData.Enabled = false;
        }

        private void lstBrends_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lstBrands.SelectedIndex == -1
            {
                return;
            }

            int selectedIndex = lstBrends.SelectedIndex;
            int selectedBrandId = Int32.Parse(dataMain.Tables[0].Rows[selectedIndex][0].ToString()); //parse: int32로 변환

            DataSet dataProducts = new DataSet();
            string query = "SELECT * FROM production.products WHERE brand_id = @brand_id";
            SqlCommand cmd = SqlCon.CreateCommand();
            cmd.Parameters.Add(new SqlParameter("@brand_id", SqlDbType.Int)).Value = selectedBrandId;
            cmd.CommandText = query;
            SqlApt.SelectCommand = cmd; //새로 나온 객체가 cmd값으로 들어가도록
            SqlApt.Fill(dataProducts);
            grdProducts.DataSource = dataProducts.Tables[0];
        }

        private void btnVIPmembers_Click(object sender, EventArgs e)
        {
            frmVIPMembers vip = new frmVIPMembers(); //새 창 생성
            vip.ShowDialog(); //새 창 보여주기
        }
    }
}
