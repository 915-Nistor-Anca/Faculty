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
        }

        private void animalBindingNavigatorSaveItem_Click(object sender, EventArgs e)
        {
            this.Validate();
            this.animalBindingSource.EndEdit();
            this.tableAdapterManager.UpdateAll(this.animalShelterDataSet);

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'animalShelterDataSet.Specie' table. You can move, or remove it, as needed.
            this.specieTableAdapter.Fill(this.animalShelterDataSet.Specie);
            // TODO: This line of code loads data into the 'animalShelterDataSet.Animal' table. You can move, or remove it, as needed.
            this.animalTableAdapter.Fill(this.animalShelterDataSet.Animal);

        }

        private void clearTextBoxes()
        {
            animalidTextBox.Clear();
            animalnameTextBox.Clear();
            animalweightTextBox.Clear();
            favouritetoyTextBox.Clear();
            genderTextBox.Clear();
            specieidTextBox.Clear();
        }

        private void parentTable_CellClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void animalDataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void specieDataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

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
                dataAdapter.InsertCommand.Parameters.Add("@si", SqlDbType.Int).Value = Int32.Parse(specieidTextBox.Text);

                connection.Open();
                dataAdapter.InsertCommand.ExecuteNonQuery();
                MessageBox.Show("Inserted successfully in the database!", "", MessageBoxButtons.OK, MessageBoxIcon.Information);
                connection.Close();


                Form1_Load(sender, e);
                clearTextBoxes();
                //DataSet dataSet = new DataSet();
                //dataAdapter.SelectCommand = new SqlCommand("select * from Animal where specieid = @id", connection);
                //int id = int.Parse(animalDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                //dataAdapter.SelectCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                //dataAdapter.Fill(dataSet);


                
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

                Form1_Load(sender, e);
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
                dataAdapter.UpdateCommand.Parameters.Add("@si", SqlDbType.Int).Value = Int32.Parse(specieidTextBox.Text);

                int id = int.Parse(animalDataGridView.SelectedRows[0].Cells[0].Value.ToString());
                dataAdapter.UpdateCommand.Parameters.Add("@id", SqlDbType.Int).Value = id;

                connection.Open();
                dataAdapter.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated succesfully to the database!");
                connection.Close();

                Form1_Load(sender, e);
                clearTextBoxes();
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "", MessageBoxButtons.OK, MessageBoxIcon.Error);
                connection.Close();
            }
        }


        private void animalnameTextBox_TextChanged(object sender, EventArgs e)
        {

        }

    }
}
