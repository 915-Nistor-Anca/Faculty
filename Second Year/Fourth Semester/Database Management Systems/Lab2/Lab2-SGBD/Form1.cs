using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Lab2_SGBD
{
    public partial class Form1 : Form
    {

        SqlConnection sqlConnection = new SqlConnection(ConfigurationManager.ConnectionStrings["cn"].ToString());
        SqlDataAdapter da = new SqlDataAdapter();
        DataSet parentDataSet = new DataSet();
        DataSet childDataSet = new DataSet();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            generateTextboxes();
            populateParentGridView();
        }
        private void generateTextboxes()
        {
            parentLabel.Text = ConfigurationManager.AppSettings["ParentTableName"].ToString();
            childLabel.Text = ConfigurationManager.AppSettings["ChildTableName"].ToString();

            List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
            int pointX = 30;
            int pointY = 40;
            childPanel.Controls.Clear();
            foreach (string column in ColumnNames)
            {
                 TextBox a = new TextBox();
                 a.Text = column;
                 a.Name = column;
                 a.Location = new Point(pointX, pointY);
                 a.Visible = true;
                 a.Parent = childPanel;
                 childPanel.Show();
                 pointY += 30;
            }

        }

        private void populateParentGridView()
        {
            try
            {
                sqlConnection.Open();
                da.SelectCommand = new SqlCommand(ConfigurationManager.AppSettings["ParentSelectQuery"].ToString(), sqlConnection);

                parentDataSet.Clear();
                da.Fill(parentDataSet);
                parentGridView.DataSource = parentDataSet.Tables[0];
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            finally
            {
                if (sqlConnection.State == ConnectionState.Open)
                {
                    sqlConnection.Close();
                }
            }
        }

        private void populateChildGridView()
        {
            try
            {
                sqlConnection.Open();
                da.SelectCommand = new SqlCommand(ConfigurationManager.AppSettings["ChildSelectQuery"].ToString(), sqlConnection);

                int parentId = int.Parse(parentGridView.SelectedRows[0].Cells[ConfigurationManager.AppSettings["ParentKeyName"].ToString()].Value.ToString());
                da.SelectCommand.Parameters.Add("@parentKey", SqlDbType.Int).Value = parentId;
                childDataSet.Clear();
                da.Fill(childDataSet);
                childGridView.DataSource = childDataSet.Tables[0];
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (sqlConnection.State == ConnectionState.Open)
                {
                    sqlConnection.Close();
                }
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            try
            {
                da.InsertCommand = new SqlCommand(ConfigurationManager.AppSettings["ChildInsertQuery"].ToString(), sqlConnection);

                int parentID = int.Parse(parentGridView.SelectedRows[0].Cells[ConfigurationManager.AppSettings["ParentKeyName"].ToString()].Value.ToString());
                da.InsertCommand.Parameters.Add("@parentKey", SqlDbType.Int).Value = parentID;

                List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                int i = 1;
                foreach (string column in ColumnNames)
                {
                    TextBox textBox = (TextBox)childPanel.Controls[column];
                    da.InsertCommand.Parameters.Add("@column" + i, SqlDbType.VarChar).Value = textBox.Text;
                    i++;
                }

                sqlConnection.Open();
                da.InsertCommand.ExecuteNonQuery();
                MessageBox.Show("Inserted successfully into the database!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (sqlConnection.State == ConnectionState.Open)
                {
                    sqlConnection.Close();
                    populateChildGridView();
                }
            }
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            try
            {
                da.UpdateCommand = new SqlCommand(ConfigurationManager.AppSettings["ChildUpdateQuery"].ToString(), sqlConnection);

                int childId = int.Parse(childGridView.SelectedRows[0].Cells[ConfigurationManager.AppSettings["ChildKeyName"].ToString()].Value.ToString());
                da.UpdateCommand.Parameters.Add("@childKey", SqlDbType.Int).Value = childId;

                List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                int i = 1;
                foreach (string column in ColumnNames)
                {
                    TextBox textBox = (TextBox)childPanel.Controls[column];
                    da.UpdateCommand.Parameters.Add("@column" + i, SqlDbType.VarChar).Value = textBox.Text;
                    i++;
                }

                sqlConnection.Open();
                da.UpdateCommand.ExecuteNonQuery();
                MessageBox.Show("Updated successfully into the database!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (sqlConnection.State == ConnectionState.Open)
                {
                    sqlConnection.Close();
                    populateChildGridView();
                }
            }
        }

        private void deleteButton_Click(object sender, EventArgs e)
        {
            try
            {
                da.DeleteCommand = new SqlCommand(ConfigurationManager.AppSettings["ChildDeleteQuery"].ToString(), sqlConnection);
                int childId = int.Parse(childGridView.SelectedRows[0].Cells[ConfigurationManager.AppSettings["ChildKeyName"].ToString()].Value.ToString());
                da.DeleteCommand.Parameters.Add("@childKey", SqlDbType.Int).Value = childId;
                sqlConnection.Open();
                da.DeleteCommand.ExecuteNonQuery();
                MessageBox.Show("Deleted successfully from the database!");
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            finally
            {
                if (sqlConnection.State == ConnectionState.Open)
                {
                    sqlConnection.Close();
                    populateChildGridView();
                }
            }
        }

        private void parentGridView_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            populateChildGridView();
        }

        private void childGridView_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            List<string> ColumnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

            foreach (string column in ColumnNames)
            {
                TextBox textBox = (TextBox)childPanel.Controls[column];
                textBox.Text = childGridView.CurrentRow.Cells[column].Value.ToString();
            }
        }

        private void parentLabel_Click(object sender, EventArgs e)
        {

        }
    }
}
