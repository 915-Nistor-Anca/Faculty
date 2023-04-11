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
using System.Data.Common;
using System.Configuration;

namespace Lab1_SGBD
{
    public partial class Form1 : Form
    {

        private SqlConnection connection = new SqlConnection("Data Source=LAPTOP-F2CFKS3J\\SQLEXPRESS01;Initial Catalog=AnimalShelter;Integrated Security=True");
        private SqlDataAdapter dataAdapter = new SqlDataAdapter();
        private DataSet dataSet1 = new DataSet(), dataSet2 = new DataSet();


        public Form1()
        {

            InitializeComponent();
            dataAdapter.SelectCommand = new SqlCommand("select * from Specie", connection);
            dataSet2.Clear();
            dataAdapter.Fill(dataSet2);
            specieDataGridView.DataSource = dataSet2.Tables[0];

        }


        private void clearTextBoxes()
        {
            animalnameTextBox.Clear();
            animalweightTextBox.Clear();
            favouritetoyTextBox.Clear();
            genderTextBox.Clear();
        }



        private void addButton_Click(object sender, EventArgs e)
        {
            try
            {
                // we create the insert command
                dataAdapter.InsertCommand = new SqlCommand("insert into Animal(animalname, animaldateofbirth, animalweight, gender, favouritetoy, specieid) values (@an, @adob, @aw, @g, @ft, @si)", connection);

                // we add the parameters of the cmd
                dataAdapter.InsertCommand.Parameters.Add("@an", SqlDbType.VarChar).Value = animalnameTextBox.Text;
                dataAdapter.InsertCommand.Parameters.Add("@adob", SqlDbType.DateTime).Value = DateTime.Parse(animaldateofbirthDateTimePicker.Text);
                dataAdapter.InsertCommand.Parameters.Add("@aw", SqlDbType.Float).Value = float.Parse(animalweightTextBox.Text);
                dataAdapter.InsertCommand.Parameters.Add("@g", SqlDbType.VarChar).Value = genderTextBox.Text;
                dataAdapter.InsertCommand.Parameters.Add("@ft", SqlDbType.VarChar).Value = favouritetoyTextBox.Text;

                dataAdapter.InsertCommand.Parameters.Add("@si", SqlDbType.Int).Value = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());

                connection.Open();
                dataAdapter.InsertCommand.ExecuteNonQuery();
                MessageBox.Show("Inserted successfully in the database!", "", MessageBoxButtons.OK, MessageBoxIcon.Information);
                connection.Close();



                dataAdapter.SelectCommand = new SqlCommand("select * from Animal where specieid = @id", connection);
                int id = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                animalDataGridView.DataSource = dataSet1.Tables[0];
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
                dataAdapter.DeleteCommand = new SqlCommand("delete from Animal where animalid = @id", connection);
                int id = int.Parse(animalDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.DeleteCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                connection.Open();
                dataAdapter.DeleteCommand.ExecuteNonQuery();
                MessageBox.Show("Deleted succesfully from the database!");
                connection.Close();


                dataAdapter.SelectCommand = new SqlCommand("select * from Animal where specieid = @id", connection);
                int id2 = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id2;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                animalDataGridView.DataSource = dataSet1.Tables[0];
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
                dataAdapter.UpdateCommand = new SqlCommand("update Animal set animalname = @an, animaldateofbirth = @adob, animalweight = @aw, gender = @g, favouritetoy = @ft, specieid = @si where animalid = @id", connection);
                dataAdapter.UpdateCommand.Parameters.Add("@an", SqlDbType.VarChar).Value = animalnameTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@adob", SqlDbType.DateTime).Value = DateTime.Parse(animaldateofbirthDateTimePicker.Text);
                dataAdapter.UpdateCommand.Parameters.Add("@aw", SqlDbType.Float).Value = float.Parse(animalweightTextBox.Text);
                dataAdapter.UpdateCommand.Parameters.Add("@g", SqlDbType.VarChar).Value = genderTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@ft", SqlDbType.VarChar).Value = favouritetoyTextBox.Text;
                dataAdapter.UpdateCommand.Parameters.Add("@si", SqlDbType.Int).Value = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());

                int id = int.Parse(animalDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                connection.Open();
                dataAdapter.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated succesfully to the database!");
                connection.Close();


                dataAdapter.SelectCommand = new SqlCommand("select * from Animal where specieid = @id", connection);
                int id2 = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id2;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                animalDataGridView.DataSource = dataSet1.Tables[0];
                clearTextBoxes();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

        private void showAnimals(object sender, DataGridViewCellMouseEventArgs e)
        {
            try
            {
                dataAdapter.SelectCommand = new SqlCommand("select * from Animal where specieid = @id", connection);
                int id = int.Parse(specieDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;
                dataSet1.Clear();
                dataAdapter.Fill(dataSet1);
                animalDataGridView.DataSource = dataSet1.Tables[0];
            }
            catch (Exception ex)
            {

                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }

        private void animalDataGridView_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            clearTextBoxes();
            string name = animalDataGridView.SelectedRows[0].Cells[1].Value.ToString();
            string date = animalDataGridView.SelectedRows[0].Cells[2].Value.ToString();
            string weight = animalDataGridView.SelectedRows[0].Cells[3].Value.ToString();
            string gender = animalDataGridView.SelectedRows[0].Cells[4].Value.ToString();
            string favourite_toy = animalDataGridView.SelectedRows[0].Cells[5].Value.ToString();

            animalnameTextBox.AppendText(name);
            animaldateofbirthDateTimePicker.Text = date;
            animalweightTextBox.AppendText(weight);
            genderTextBox.AppendText(gender);
            favouritetoyTextBox.AppendText(favourite_toy);


        }

        private void animalnameTextBox_TextChanged(object sender, EventArgs e)
        {

        }

    }
}
