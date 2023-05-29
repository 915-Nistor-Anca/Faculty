using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Practic_SGBD
{
    public partial class Form1 : Form
    {
        private SqlConnection connection = new SqlConnection("Data Source=LAPTOP-F2CFKS3J\\SQLEXPRESS01;Initial Catalog=PracticalExam;Integrated Security=True");
        private SqlDataAdapter dataAdapter = new SqlDataAdapter();
        private DataSet dataSet1 = new DataSet(), dataSet2 = new DataSet();

        public Form1()
        {
            InitializeComponent();
            dataAdapter.SelectCommand = new SqlCommand("select * from Sport", connection);
            dataSet2.Clear();
            dataAdapter.Fill(dataSet2);
            sportDataGridView.DataSource = dataSet2.Tables[0];
        }

        private void clearTextBoxes()
        {
            teamnameTextBox.Clear();
            teammembersTextBox.Clear();
            teamyearTextBox.Clear();
            teamcityTextBox.Clear();
            teamtypeTextBox.Clear();
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            try
            {
                // we create the insert command
                dataAdapter.InsertCommand = new SqlCommand("insert into Team(teamname, numberofmembers, startupyear, city, typeid, sportid) values (@an, @adob, @aw, @g, @ft, @si)", connection);

                // we add the parameters of the cmd
                dataAdapter.InsertCommand.Parameters.Add("@an", SqlDbType.VarChar).Value = teamnameTextBox.Text;
                dataAdapter.InsertCommand.Parameters.Add("@adob", SqlDbType.Float).Value = int.Parse(teammembersTextBox.Text);
                dataAdapter.InsertCommand.Parameters.Add("@aw", SqlDbType.Float).Value = int.Parse(teamyearTextBox.Text);
                dataAdapter.InsertCommand.Parameters.Add("@g", SqlDbType.VarChar).Value = teamcityTextBox.Text;
                dataAdapter.InsertCommand.Parameters.Add("@ft", SqlDbType.VarChar).Value = teamtypeTextBox.Text;

                dataAdapter.InsertCommand.Parameters.Add("@si", SqlDbType.Int).Value = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());

                connection.Open();
                dataAdapter.InsertCommand.ExecuteNonQuery();
                MessageBox.Show("Inserted successfully in the database!", "", MessageBoxButtons.OK, MessageBoxIcon.Information);
                connection.Close();



                dataAdapter.SelectCommand = new SqlCommand("select * from Team where sportid = @id", connection);
                int id = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                teamDataGridView.DataSource = dataSet1.Tables[0];
                clearTextBoxes();




            }
            catch (Exception ex)
            {

                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            try
            {
                dataAdapter.DeleteCommand = new SqlCommand("delete from Team where teamid = @id", connection);
                int id = int.Parse(teamDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                connection.Open();
                dataAdapter.DeleteCommand.ExecuteNonQuery();
                MessageBox.Show("Deleted succesfully from the database!");
                connection.Close();


                dataAdapter.SelectCommand = new SqlCommand("select * from Team where sportid = @id", connection);
                int id2 = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id2;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                teamDataGridView.DataSource = dataSet1.Tables[0];
                clearTextBoxes();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

     
        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                dataAdapter.UpdateCommand = new SqlCommand("update Team set teamname = @an, numberofmembers = @adob, startupyear = @aw, city = @g, typeid = @ft, sportid = @si where teamid = @id", connection);

                dataAdapter.UpdateCommand.Parameters.Add("@an", SqlDbType.VarChar).Value = teamnameTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@adob", SqlDbType.Float).Value = float.Parse(teammembersTextBox.Text);
                dataAdapter.UpdateCommand.Parameters.Add("@aw", SqlDbType.Float).Value = float.Parse(teamyearTextBox.Text);
                dataAdapter.UpdateCommand.Parameters.Add("@g", SqlDbType.VarChar).Value = teamcityTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@ft", SqlDbType.VarChar).Value = teamtypeTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@si", SqlDbType.Int).Value = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());


                int id = int.Parse(teamDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                connection.Open();
                dataAdapter.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated succesfully to the database!");
                connection.Close();


                dataAdapter.SelectCommand = new SqlCommand("select * from Team where teamid = @id", connection);
                int id2 = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id2;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                teamDataGridView.DataSource = dataSet1.Tables[0];
                clearTextBoxes();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void teamDataGridView_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            clearTextBoxes();
            string name = teamDataGridView.SelectedRows[0].Cells[1].Value.ToString();
            string members = teamDataGridView.SelectedRows[0].Cells[2].Value.ToString();
            string year = teamDataGridView.SelectedRows[0].Cells[3].Value.ToString();
            string city = teamDataGridView.SelectedRows[0].Cells[4].Value.ToString();
            string typeid = teamDataGridView.SelectedRows[0].Cells[5].Value.ToString();

            teamnameTextBox.AppendText(name);
            teammembersTextBox.AppendText(members);
            teamyearTextBox.AppendText(year);
            teamcityTextBox.AppendText(city);
            teamtypeTextBox.AppendText(typeid);
        }

        private void sportDataGridView_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            try
            {
                dataAdapter.SelectCommand = new SqlCommand("select * from Team where sportid = @id", connection);
                int id = int.Parse(sportDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                teamDataGridView.DataSource = dataSet1.Tables[0];
            }
            catch (Exception ex)
            {

                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    
    }
}
