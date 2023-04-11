namespace Lab1_SGBD
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.Windows.Forms.Label animalnameLabel;
            System.Windows.Forms.Label animaldateofbirthLabel;
            System.Windows.Forms.Label animalweightLabel;
            System.Windows.Forms.Label genderLabel;
            System.Windows.Forms.Label favouritetoyLabel;
            this.animalShelterDataSet = new Lab1_SGBD.AnimalShelterDataSet();
            this.animalBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.animalTableAdapter = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.AnimalTableAdapter();
            this.tableAdapterManager = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.TableAdapterManager();
            this.specieBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.specieTableAdapter = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.SpecieTableAdapter();
            this.specieDataGridView = new System.Windows.Forms.DataGridView();
            this.animalBindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.animalDataGridView = new System.Windows.Forms.DataGridView();
            this.animalnameTextBox = new System.Windows.Forms.TextBox();
            this.animaldateofbirthDateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.animalweightTextBox = new System.Windows.Forms.TextBox();
            this.genderTextBox = new System.Windows.Forms.TextBox();
            this.favouritetoyTextBox = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            animalnameLabel = new System.Windows.Forms.Label();
            animaldateofbirthLabel = new System.Windows.Forms.Label();
            animalweightLabel = new System.Windows.Forms.Label();
            genderLabel = new System.Windows.Forms.Label();
            favouritetoyLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.animalShelterDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.specieBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.specieDataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalDataGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // animalnameLabel
            // 
            animalnameLabel.AutoSize = true;
            animalnameLabel.Location = new System.Drawing.Point(68, 347);
            animalnameLabel.Name = "animalnameLabel";
            animalnameLabel.Size = new System.Drawing.Size(84, 16);
            animalnameLabel.TabIndex = 18;
            animalnameLabel.Text = "animalname:";
            // 
            // animaldateofbirthLabel
            // 
            animaldateofbirthLabel.AutoSize = true;
            animaldateofbirthLabel.Location = new System.Drawing.Point(68, 376);
            animaldateofbirthLabel.Name = "animaldateofbirthLabel";
            animaldateofbirthLabel.Size = new System.Drawing.Size(113, 16);
            animaldateofbirthLabel.TabIndex = 20;
            animaldateofbirthLabel.Text = "animaldateofbirth:";
            // 
            // animalweightLabel
            // 
            animalweightLabel.AutoSize = true;
            animalweightLabel.Location = new System.Drawing.Point(68, 403);
            animalweightLabel.Name = "animalweightLabel";
            animalweightLabel.Size = new System.Drawing.Size(88, 16);
            animalweightLabel.TabIndex = 22;
            animalweightLabel.Text = "animalweight:";
            // 
            // genderLabel
            // 
            genderLabel.AutoSize = true;
            genderLabel.Location = new System.Drawing.Point(68, 431);
            genderLabel.Name = "genderLabel";
            genderLabel.Size = new System.Drawing.Size(53, 16);
            genderLabel.TabIndex = 24;
            genderLabel.Text = "gender:";
            // 
            // favouritetoyLabel
            // 
            favouritetoyLabel.AutoSize = true;
            favouritetoyLabel.Location = new System.Drawing.Point(68, 459);
            favouritetoyLabel.Name = "favouritetoyLabel";
            favouritetoyLabel.Size = new System.Drawing.Size(79, 16);
            favouritetoyLabel.TabIndex = 26;
            favouritetoyLabel.Text = "favouritetoy:";
            // 
            // animalShelterDataSet
            // 
            this.animalShelterDataSet.DataSetName = "AnimalShelterDataSet";
            this.animalShelterDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema;
            // 
            // animalBindingSource
            // 
            this.animalBindingSource.DataMember = "Animal";
            this.animalBindingSource.DataSource = this.animalShelterDataSet;
            // 
            // animalTableAdapter
            // 
            this.animalTableAdapter.ClearBeforeFill = true;
            // 
            // tableAdapterManager
            // 
            this.tableAdapterManager.AnimalTableAdapter = this.animalTableAdapter;
            this.tableAdapterManager.BackupDataSetBeforeUpdate = false;
            this.tableAdapterManager.SpecieTableAdapter = null;
            this.tableAdapterManager.UpdateOrder = Lab1_SGBD.AnimalShelterDataSetTableAdapters.TableAdapterManager.UpdateOrderOption.InsertUpdateDelete;
            // 
            // specieBindingSource
            // 
            this.specieBindingSource.DataMember = "Specie";
            this.specieBindingSource.DataSource = this.animalShelterDataSet;
            // 
            // specieTableAdapter
            // 
            this.specieTableAdapter.ClearBeforeFill = true;
            // 
            // specieDataGridView
            // 
            this.specieDataGridView.AllowUserToAddRows = false;
            this.specieDataGridView.AllowUserToDeleteRows = false;
            this.specieDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.specieDataGridView.Location = new System.Drawing.Point(555, 344);
            this.specieDataGridView.Name = "specieDataGridView";
            this.specieDataGridView.ReadOnly = true;
            this.specieDataGridView.RowHeadersWidth = 51;
            this.specieDataGridView.RowTemplate.Height = 24;
            this.specieDataGridView.Size = new System.Drawing.Size(640, 220);
            this.specieDataGridView.TabIndex = 16;
            this.specieDataGridView.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.showAnimals);
            // 
            // animalBindingSource1
            // 
            this.animalBindingSource1.DataMember = "FK__Animal__specieid__3B75D760";
            this.animalBindingSource1.DataSource = this.specieBindingSource;
            // 
            // animalDataGridView
            // 
            this.animalDataGridView.AllowUserToAddRows = false;
            this.animalDataGridView.AllowUserToDeleteRows = false;
            this.animalDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.animalDataGridView.Location = new System.Drawing.Point(25, 53);
            this.animalDataGridView.Name = "animalDataGridView";
            this.animalDataGridView.ReadOnly = true;
            this.animalDataGridView.RowHeadersWidth = 51;
            this.animalDataGridView.RowTemplate.Height = 24;
            this.animalDataGridView.Size = new System.Drawing.Size(1256, 242);
            this.animalDataGridView.TabIndex = 16;
            this.animalDataGridView.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.animalDataGridView_RowHeaderMouseClick);
            // 
            // animalnameTextBox
            // 
            this.animalnameTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "animalname", true));
            this.animalnameTextBox.Location = new System.Drawing.Point(187, 344);
            this.animalnameTextBox.Name = "animalnameTextBox";
            this.animalnameTextBox.Size = new System.Drawing.Size(200, 22);
            this.animalnameTextBox.TabIndex = 19;
            this.animalnameTextBox.TextChanged += new System.EventHandler(this.animalnameTextBox_TextChanged);
            // 
            // animaldateofbirthDateTimePicker
            // 
            this.animaldateofbirthDateTimePicker.DataBindings.Add(new System.Windows.Forms.Binding("Value", this.animalBindingSource1, "animaldateofbirth", true));
            this.animaldateofbirthDateTimePicker.Location = new System.Drawing.Point(187, 372);
            this.animaldateofbirthDateTimePicker.Name = "animaldateofbirthDateTimePicker";
            this.animaldateofbirthDateTimePicker.Size = new System.Drawing.Size(200, 22);
            this.animaldateofbirthDateTimePicker.TabIndex = 21;
            // 
            // animalweightTextBox
            // 
            this.animalweightTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "animalweight", true));
            this.animalweightTextBox.Location = new System.Drawing.Point(187, 400);
            this.animalweightTextBox.Name = "animalweightTextBox";
            this.animalweightTextBox.Size = new System.Drawing.Size(200, 22);
            this.animalweightTextBox.TabIndex = 23;
            // 
            // genderTextBox
            // 
            this.genderTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "gender", true));
            this.genderTextBox.Location = new System.Drawing.Point(187, 428);
            this.genderTextBox.Name = "genderTextBox";
            this.genderTextBox.Size = new System.Drawing.Size(200, 22);
            this.genderTextBox.TabIndex = 25;
            // 
            // favouritetoyTextBox
            // 
            this.favouritetoyTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "favouritetoy", true));
            this.favouritetoyTextBox.Location = new System.Drawing.Point(187, 456);
            this.favouritetoyTextBox.Name = "favouritetoyTextBox";
            this.favouritetoyTextBox.Size = new System.Drawing.Size(200, 22);
            this.favouritetoyTextBox.TabIndex = 27;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(71, 565);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(109, 44);
            this.button1.TabIndex = 30;
            this.button1.Text = "Add";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.addButton_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(176, 565);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(98, 44);
            this.button2.TabIndex = 31;
            this.button2.Text = "Remove";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.removeButton_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(271, 565);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(94, 44);
            this.button3.TabIndex = 32;
            this.button3.Text = "Update";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1306, 661);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(animalnameLabel);
            this.Controls.Add(this.animalnameTextBox);
            this.Controls.Add(animaldateofbirthLabel);
            this.Controls.Add(this.animaldateofbirthDateTimePicker);
            this.Controls.Add(animalweightLabel);
            this.Controls.Add(this.animalweightTextBox);
            this.Controls.Add(genderLabel);
            this.Controls.Add(this.genderTextBox);
            this.Controls.Add(favouritetoyLabel);
            this.Controls.Add(this.favouritetoyTextBox);
            this.Controls.Add(this.animalDataGridView);
            this.Controls.Add(this.specieDataGridView);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.animalShelterDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.specieBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.specieDataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalDataGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private AnimalShelterDataSet animalShelterDataSet;
        private System.Windows.Forms.BindingSource animalBindingSource;
        private AnimalShelterDataSetTableAdapters.AnimalTableAdapter animalTableAdapter;
        private AnimalShelterDataSetTableAdapters.TableAdapterManager tableAdapterManager;
        private System.Windows.Forms.BindingSource specieBindingSource;
        private AnimalShelterDataSetTableAdapters.SpecieTableAdapter specieTableAdapter;
        private System.Windows.Forms.DataGridView specieDataGridView;
        private System.Windows.Forms.BindingSource animalBindingSource1;
        private System.Windows.Forms.DataGridView animalDataGridView;
        private System.Windows.Forms.TextBox animalnameTextBox;
        private System.Windows.Forms.DateTimePicker animaldateofbirthDateTimePicker;
        private System.Windows.Forms.TextBox animalweightTextBox;
        private System.Windows.Forms.TextBox genderTextBox;
        private System.Windows.Forms.TextBox favouritetoyTextBox;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
    }
}

