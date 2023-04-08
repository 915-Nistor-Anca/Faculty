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
            System.Windows.Forms.Label animalidLabel;
            System.Windows.Forms.Label animalnameLabel;
            System.Windows.Forms.Label animaldateofbirthLabel;
            System.Windows.Forms.Label animalweightLabel;
            System.Windows.Forms.Label genderLabel;
            System.Windows.Forms.Label favouritetoyLabel;
            System.Windows.Forms.Label specieidLabel;
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.animalShelterDataSet = new Lab1_SGBD.AnimalShelterDataSet();
            this.animalBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.animalTableAdapter = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.AnimalTableAdapter();
            this.tableAdapterManager = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.TableAdapterManager();
            this.animalBindingNavigator = new System.Windows.Forms.BindingNavigator(this.components);
            this.bindingNavigatorAddNewItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorCountItem = new System.Windows.Forms.ToolStripLabel();
            this.bindingNavigatorDeleteItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveFirstItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMovePreviousItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorPositionItem = new System.Windows.Forms.ToolStripTextBox();
            this.bindingNavigatorSeparator1 = new System.Windows.Forms.ToolStripSeparator();
            this.bindingNavigatorMoveNextItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorMoveLastItem = new System.Windows.Forms.ToolStripButton();
            this.bindingNavigatorSeparator2 = new System.Windows.Forms.ToolStripSeparator();
            this.animalBindingNavigatorSaveItem = new System.Windows.Forms.ToolStripButton();
            this.specieBindingSource = new System.Windows.Forms.BindingSource(this.components);
            this.specieTableAdapter = new Lab1_SGBD.AnimalShelterDataSetTableAdapters.SpecieTableAdapter();
            this.specieDataGridView = new System.Windows.Forms.DataGridView();
            this.dataGridViewTextBoxColumn8 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn9 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn10 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.animalBindingSource1 = new System.Windows.Forms.BindingSource(this.components);
            this.animalDataGridView = new System.Windows.Forms.DataGridView();
            this.dataGridViewTextBoxColumn1 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn2 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn3 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn4 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn5 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn6 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.dataGridViewTextBoxColumn7 = new System.Windows.Forms.DataGridViewTextBoxColumn();
            this.animalidTextBox = new System.Windows.Forms.TextBox();
            this.animalnameTextBox = new System.Windows.Forms.TextBox();
            this.animaldateofbirthDateTimePicker = new System.Windows.Forms.DateTimePicker();
            this.animalweightTextBox = new System.Windows.Forms.TextBox();
            this.genderTextBox = new System.Windows.Forms.TextBox();
            this.favouritetoyTextBox = new System.Windows.Forms.TextBox();
            this.specieidTextBox = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            animalidLabel = new System.Windows.Forms.Label();
            animalnameLabel = new System.Windows.Forms.Label();
            animaldateofbirthLabel = new System.Windows.Forms.Label();
            animalweightLabel = new System.Windows.Forms.Label();
            genderLabel = new System.Windows.Forms.Label();
            favouritetoyLabel = new System.Windows.Forms.Label();
            specieidLabel = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.animalShelterDataSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingNavigator)).BeginInit();
            this.animalBindingNavigator.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.specieBindingSource)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.specieDataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalDataGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // animalidLabel
            // 
            animalidLabel.AutoSize = true;
            animalidLabel.Location = new System.Drawing.Point(68, 319);
            animalidLabel.Name = "animalidLabel";
            animalidLabel.Size = new System.Drawing.Size(61, 16);
            animalidLabel.TabIndex = 16;
            animalidLabel.Text = "animalid:";
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
            // specieidLabel
            // 
            specieidLabel.AutoSize = true;
            specieidLabel.Location = new System.Drawing.Point(68, 487);
            specieidLabel.Name = "specieidLabel";
            specieidLabel.Size = new System.Drawing.Size(62, 16);
            specieidLabel.TabIndex = 28;
            specieidLabel.Text = "specieid:";
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
            // animalBindingNavigator
            // 
            this.animalBindingNavigator.AddNewItem = this.bindingNavigatorAddNewItem;
            this.animalBindingNavigator.BindingSource = this.animalBindingSource;
            this.animalBindingNavigator.CountItem = this.bindingNavigatorCountItem;
            this.animalBindingNavigator.DeleteItem = this.bindingNavigatorDeleteItem;
            this.animalBindingNavigator.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.animalBindingNavigator.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bindingNavigatorMoveFirstItem,
            this.bindingNavigatorMovePreviousItem,
            this.bindingNavigatorSeparator,
            this.bindingNavigatorPositionItem,
            this.bindingNavigatorCountItem,
            this.bindingNavigatorSeparator1,
            this.bindingNavigatorMoveNextItem,
            this.bindingNavigatorMoveLastItem,
            this.bindingNavigatorSeparator2,
            this.bindingNavigatorAddNewItem,
            this.bindingNavigatorDeleteItem,
            this.animalBindingNavigatorSaveItem});
            this.animalBindingNavigator.Location = new System.Drawing.Point(0, 0);
            this.animalBindingNavigator.MoveFirstItem = this.bindingNavigatorMoveFirstItem;
            this.animalBindingNavigator.MoveLastItem = this.bindingNavigatorMoveLastItem;
            this.animalBindingNavigator.MoveNextItem = this.bindingNavigatorMoveNextItem;
            this.animalBindingNavigator.MovePreviousItem = this.bindingNavigatorMovePreviousItem;
            this.animalBindingNavigator.Name = "animalBindingNavigator";
            this.animalBindingNavigator.PositionItem = this.bindingNavigatorPositionItem;
            this.animalBindingNavigator.Size = new System.Drawing.Size(1319, 27);
            this.animalBindingNavigator.TabIndex = 0;
            this.animalBindingNavigator.Text = "bindingNavigator1";
            // 
            // bindingNavigatorAddNewItem
            // 
            this.bindingNavigatorAddNewItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorAddNewItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorAddNewItem.Image")));
            this.bindingNavigatorAddNewItem.Name = "bindingNavigatorAddNewItem";
            this.bindingNavigatorAddNewItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorAddNewItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorAddNewItem.Text = "Add new";
            // 
            // bindingNavigatorCountItem
            // 
            this.bindingNavigatorCountItem.Name = "bindingNavigatorCountItem";
            this.bindingNavigatorCountItem.Size = new System.Drawing.Size(45, 24);
            this.bindingNavigatorCountItem.Text = "of {0}";
            this.bindingNavigatorCountItem.ToolTipText = "Total number of items";
            // 
            // bindingNavigatorDeleteItem
            // 
            this.bindingNavigatorDeleteItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorDeleteItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorDeleteItem.Image")));
            this.bindingNavigatorDeleteItem.Name = "bindingNavigatorDeleteItem";
            this.bindingNavigatorDeleteItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorDeleteItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorDeleteItem.Text = "Delete";
            // 
            // bindingNavigatorMoveFirstItem
            // 
            this.bindingNavigatorMoveFirstItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveFirstItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveFirstItem.Image")));
            this.bindingNavigatorMoveFirstItem.Name = "bindingNavigatorMoveFirstItem";
            this.bindingNavigatorMoveFirstItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveFirstItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveFirstItem.Text = "Move first";
            // 
            // bindingNavigatorMovePreviousItem
            // 
            this.bindingNavigatorMovePreviousItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMovePreviousItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMovePreviousItem.Image")));
            this.bindingNavigatorMovePreviousItem.Name = "bindingNavigatorMovePreviousItem";
            this.bindingNavigatorMovePreviousItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMovePreviousItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMovePreviousItem.Text = "Move previous";
            // 
            // bindingNavigatorSeparator
            // 
            this.bindingNavigatorSeparator.Name = "bindingNavigatorSeparator";
            this.bindingNavigatorSeparator.Size = new System.Drawing.Size(6, 27);
            // 
            // bindingNavigatorPositionItem
            // 
            this.bindingNavigatorPositionItem.AccessibleName = "Position";
            this.bindingNavigatorPositionItem.AutoSize = false;
            this.bindingNavigatorPositionItem.Font = new System.Drawing.Font("Segoe UI", 9F);
            this.bindingNavigatorPositionItem.Name = "bindingNavigatorPositionItem";
            this.bindingNavigatorPositionItem.Size = new System.Drawing.Size(50, 27);
            this.bindingNavigatorPositionItem.Text = "0";
            this.bindingNavigatorPositionItem.ToolTipText = "Current position";
            // 
            // bindingNavigatorSeparator1
            // 
            this.bindingNavigatorSeparator1.Name = "bindingNavigatorSeparator1";
            this.bindingNavigatorSeparator1.Size = new System.Drawing.Size(6, 27);
            // 
            // bindingNavigatorMoveNextItem
            // 
            this.bindingNavigatorMoveNextItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveNextItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveNextItem.Image")));
            this.bindingNavigatorMoveNextItem.Name = "bindingNavigatorMoveNextItem";
            this.bindingNavigatorMoveNextItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveNextItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveNextItem.Text = "Move next";
            // 
            // bindingNavigatorMoveLastItem
            // 
            this.bindingNavigatorMoveLastItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.bindingNavigatorMoveLastItem.Image = ((System.Drawing.Image)(resources.GetObject("bindingNavigatorMoveLastItem.Image")));
            this.bindingNavigatorMoveLastItem.Name = "bindingNavigatorMoveLastItem";
            this.bindingNavigatorMoveLastItem.RightToLeftAutoMirrorImage = true;
            this.bindingNavigatorMoveLastItem.Size = new System.Drawing.Size(29, 24);
            this.bindingNavigatorMoveLastItem.Text = "Move last";
            // 
            // bindingNavigatorSeparator2
            // 
            this.bindingNavigatorSeparator2.Name = "bindingNavigatorSeparator2";
            this.bindingNavigatorSeparator2.Size = new System.Drawing.Size(6, 27);
            // 
            // animalBindingNavigatorSaveItem
            // 
            this.animalBindingNavigatorSaveItem.DisplayStyle = System.Windows.Forms.ToolStripItemDisplayStyle.Image;
            this.animalBindingNavigatorSaveItem.Image = ((System.Drawing.Image)(resources.GetObject("animalBindingNavigatorSaveItem.Image")));
            this.animalBindingNavigatorSaveItem.Name = "animalBindingNavigatorSaveItem";
            this.animalBindingNavigatorSaveItem.Size = new System.Drawing.Size(29, 24);
            this.animalBindingNavigatorSaveItem.Text = "Save Data";
            this.animalBindingNavigatorSaveItem.Click += new System.EventHandler(this.animalBindingNavigatorSaveItem_Click);
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
            this.specieDataGridView.AutoGenerateColumns = false;
            this.specieDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.specieDataGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dataGridViewTextBoxColumn8,
            this.dataGridViewTextBoxColumn9,
            this.dataGridViewTextBoxColumn10});
            this.specieDataGridView.DataSource = this.specieBindingSource;
            this.specieDataGridView.Location = new System.Drawing.Point(469, 316);
            this.specieDataGridView.Name = "specieDataGridView";
            this.specieDataGridView.RowHeadersWidth = 51;
            this.specieDataGridView.RowTemplate.Height = 24;
            this.specieDataGridView.Size = new System.Drawing.Size(442, 220);
            this.specieDataGridView.TabIndex = 16;
            this.specieDataGridView.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.specieDataGridView_CellContentClick);
            // 
            // dataGridViewTextBoxColumn8
            // 
            this.dataGridViewTextBoxColumn8.DataPropertyName = "specieid";
            this.dataGridViewTextBoxColumn8.HeaderText = "specieid";
            this.dataGridViewTextBoxColumn8.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn8.Name = "dataGridViewTextBoxColumn8";
            this.dataGridViewTextBoxColumn8.ReadOnly = true;
            this.dataGridViewTextBoxColumn8.Width = 125;
            // 
            // dataGridViewTextBoxColumn9
            // 
            this.dataGridViewTextBoxColumn9.DataPropertyName = "speciename";
            this.dataGridViewTextBoxColumn9.HeaderText = "speciename";
            this.dataGridViewTextBoxColumn9.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn9.Name = "dataGridViewTextBoxColumn9";
            this.dataGridViewTextBoxColumn9.Width = 125;
            // 
            // dataGridViewTextBoxColumn10
            // 
            this.dataGridViewTextBoxColumn10.DataPropertyName = "speciespecifications";
            this.dataGridViewTextBoxColumn10.HeaderText = "speciespecifications";
            this.dataGridViewTextBoxColumn10.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn10.Name = "dataGridViewTextBoxColumn10";
            this.dataGridViewTextBoxColumn10.Width = 125;
            // 
            // animalBindingSource1
            // 
            this.animalBindingSource1.DataMember = "FK__Animal__specieid__3B75D760";
            this.animalBindingSource1.DataSource = this.specieBindingSource;
            // 
            // animalDataGridView
            // 
            this.animalDataGridView.AutoGenerateColumns = false;
            this.animalDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.animalDataGridView.Columns.AddRange(new System.Windows.Forms.DataGridViewColumn[] {
            this.dataGridViewTextBoxColumn1,
            this.dataGridViewTextBoxColumn2,
            this.dataGridViewTextBoxColumn3,
            this.dataGridViewTextBoxColumn4,
            this.dataGridViewTextBoxColumn5,
            this.dataGridViewTextBoxColumn6,
            this.dataGridViewTextBoxColumn7});
            this.animalDataGridView.DataSource = this.animalBindingSource1;
            this.animalDataGridView.Location = new System.Drawing.Point(25, 53);
            this.animalDataGridView.Name = "animalDataGridView";
            this.animalDataGridView.RowHeadersWidth = 51;
            this.animalDataGridView.RowTemplate.Height = 24;
            this.animalDataGridView.Size = new System.Drawing.Size(1256, 220);
            this.animalDataGridView.TabIndex = 16;
            // 
            // dataGridViewTextBoxColumn1
            // 
            this.dataGridViewTextBoxColumn1.DataPropertyName = "animalid";
            this.dataGridViewTextBoxColumn1.HeaderText = "animalid";
            this.dataGridViewTextBoxColumn1.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn1.Name = "dataGridViewTextBoxColumn1";
            this.dataGridViewTextBoxColumn1.ReadOnly = true;
            this.dataGridViewTextBoxColumn1.Width = 125;
            // 
            // dataGridViewTextBoxColumn2
            // 
            this.dataGridViewTextBoxColumn2.DataPropertyName = "animalname";
            this.dataGridViewTextBoxColumn2.HeaderText = "animalname";
            this.dataGridViewTextBoxColumn2.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn2.Name = "dataGridViewTextBoxColumn2";
            this.dataGridViewTextBoxColumn2.Width = 125;
            // 
            // dataGridViewTextBoxColumn3
            // 
            this.dataGridViewTextBoxColumn3.DataPropertyName = "animaldateofbirth";
            this.dataGridViewTextBoxColumn3.HeaderText = "animaldateofbirth";
            this.dataGridViewTextBoxColumn3.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn3.Name = "dataGridViewTextBoxColumn3";
            this.dataGridViewTextBoxColumn3.Width = 125;
            // 
            // dataGridViewTextBoxColumn4
            // 
            this.dataGridViewTextBoxColumn4.DataPropertyName = "animalweight";
            this.dataGridViewTextBoxColumn4.HeaderText = "animalweight";
            this.dataGridViewTextBoxColumn4.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn4.Name = "dataGridViewTextBoxColumn4";
            this.dataGridViewTextBoxColumn4.Width = 125;
            // 
            // dataGridViewTextBoxColumn5
            // 
            this.dataGridViewTextBoxColumn5.DataPropertyName = "gender";
            this.dataGridViewTextBoxColumn5.HeaderText = "gender";
            this.dataGridViewTextBoxColumn5.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn5.Name = "dataGridViewTextBoxColumn5";
            this.dataGridViewTextBoxColumn5.Width = 125;
            // 
            // dataGridViewTextBoxColumn6
            // 
            this.dataGridViewTextBoxColumn6.DataPropertyName = "favouritetoy";
            this.dataGridViewTextBoxColumn6.HeaderText = "favouritetoy";
            this.dataGridViewTextBoxColumn6.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn6.Name = "dataGridViewTextBoxColumn6";
            this.dataGridViewTextBoxColumn6.Width = 125;
            // 
            // dataGridViewTextBoxColumn7
            // 
            this.dataGridViewTextBoxColumn7.DataPropertyName = "specieid";
            this.dataGridViewTextBoxColumn7.HeaderText = "specieid";
            this.dataGridViewTextBoxColumn7.MinimumWidth = 6;
            this.dataGridViewTextBoxColumn7.Name = "dataGridViewTextBoxColumn7";
            this.dataGridViewTextBoxColumn7.Width = 125;
            // 
            // animalidTextBox
            // 
            this.animalidTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "animalid", true));
            this.animalidTextBox.Location = new System.Drawing.Point(187, 316);
            this.animalidTextBox.Name = "animalidTextBox";
            this.animalidTextBox.Size = new System.Drawing.Size(200, 22);
            this.animalidTextBox.TabIndex = 17;
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
            // specieidTextBox
            // 
            this.specieidTextBox.DataBindings.Add(new System.Windows.Forms.Binding("Text", this.animalBindingSource1, "specieid", true));
            this.specieidTextBox.Location = new System.Drawing.Point(187, 484);
            this.specieidTextBox.Name = "specieidTextBox";
            this.specieidTextBox.Size = new System.Drawing.Size(200, 22);
            this.specieidTextBox.TabIndex = 29;
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
            this.ClientSize = new System.Drawing.Size(1319, 661);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(animalidLabel);
            this.Controls.Add(this.animalidTextBox);
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
            this.Controls.Add(specieidLabel);
            this.Controls.Add(this.specieidTextBox);
            this.Controls.Add(this.animalDataGridView);
            this.Controls.Add(this.specieDataGridView);
            this.Controls.Add(this.animalBindingNavigator);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.animalShelterDataSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingSource)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.animalBindingNavigator)).EndInit();
            this.animalBindingNavigator.ResumeLayout(false);
            this.animalBindingNavigator.PerformLayout();
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
        private System.Windows.Forms.BindingNavigator animalBindingNavigator;
        private System.Windows.Forms.ToolStripButton bindingNavigatorAddNewItem;
        private System.Windows.Forms.ToolStripLabel bindingNavigatorCountItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorDeleteItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveFirstItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMovePreviousItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator;
        private System.Windows.Forms.ToolStripTextBox bindingNavigatorPositionItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator1;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveNextItem;
        private System.Windows.Forms.ToolStripButton bindingNavigatorMoveLastItem;
        private System.Windows.Forms.ToolStripSeparator bindingNavigatorSeparator2;
        private System.Windows.Forms.ToolStripButton animalBindingNavigatorSaveItem;
        private System.Windows.Forms.BindingSource specieBindingSource;
        private AnimalShelterDataSetTableAdapters.SpecieTableAdapter specieTableAdapter;
        private System.Windows.Forms.DataGridView specieDataGridView;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn8;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn9;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn10;
        private System.Windows.Forms.BindingSource animalBindingSource1;
        private System.Windows.Forms.DataGridView animalDataGridView;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn1;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn2;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn3;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn4;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn5;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn6;
        private System.Windows.Forms.DataGridViewTextBoxColumn dataGridViewTextBoxColumn7;
        private System.Windows.Forms.TextBox animalidTextBox;
        private System.Windows.Forms.TextBox animalnameTextBox;
        private System.Windows.Forms.DateTimePicker animaldateofbirthDateTimePicker;
        private System.Windows.Forms.TextBox animalweightTextBox;
        private System.Windows.Forms.TextBox genderTextBox;
        private System.Windows.Forms.TextBox favouritetoyTextBox;
        private System.Windows.Forms.TextBox specieidTextBox;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
    }
}

