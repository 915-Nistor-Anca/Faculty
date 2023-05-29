namespace Practic_SGBD
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
            this.teamnameTextBox = new System.Windows.Forms.TextBox();
            this.teamDataGridView = new System.Windows.Forms.DataGridView();
            this.label1 = new System.Windows.Forms.Label();
            this.sportDataGridView = new System.Windows.Forms.DataGridView();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.button3 = new System.Windows.Forms.Button();
            this.teammembersTextBox = new System.Windows.Forms.TextBox();
            this.teamyearTextBox = new System.Windows.Forms.TextBox();
            this.teamcityTextBox = new System.Windows.Forms.TextBox();
            this.teamtypeTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.teamDataGridView)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.sportDataGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // teamnameTextBox
            // 
            this.teamnameTextBox.Location = new System.Drawing.Point(121, 320);
            this.teamnameTextBox.Name = "teamnameTextBox";
            this.teamnameTextBox.Size = new System.Drawing.Size(100, 22);
            this.teamnameTextBox.TabIndex = 0;
            // 
            // teamDataGridView
            // 
            this.teamDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.teamDataGridView.Location = new System.Drawing.Point(25, 25);
            this.teamDataGridView.Name = "teamDataGridView";
            this.teamDataGridView.RowHeadersWidth = 51;
            this.teamDataGridView.RowTemplate.Height = 24;
            this.teamDataGridView.Size = new System.Drawing.Size(1037, 209);
            this.teamDataGridView.TabIndex = 1;
            this.teamDataGridView.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.teamDataGridView_RowHeaderMouseClick);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(41, 320);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(41, 16);
            this.label1.TabIndex = 2;
            this.label1.Text = "name";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // sportDataGridView
            // 
            this.sportDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.sportDataGridView.Location = new System.Drawing.Point(642, 277);
            this.sportDataGridView.Name = "sportDataGridView";
            this.sportDataGridView.RowHeadersWidth = 51;
            this.sportDataGridView.RowTemplate.Height = 24;
            this.sportDataGridView.Size = new System.Drawing.Size(733, 226);
            this.sportDataGridView.TabIndex = 3;
            this.sportDataGridView.RowHeaderMouseClick += new System.Windows.Forms.DataGridViewCellMouseEventHandler(this.sportDataGridView_RowHeaderMouseClick);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(55, 456);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(75, 23);
            this.button1.TabIndex = 4;
            this.button1.Text = "Add";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.addButton_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(158, 456);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(75, 23);
            this.button2.TabIndex = 5;
            this.button2.Text = "Remove";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.removeButton_Click);
            // 
            // button3
            // 
            this.button3.Location = new System.Drawing.Point(269, 456);
            this.button3.Name = "button3";
            this.button3.Size = new System.Drawing.Size(75, 23);
            this.button3.TabIndex = 6;
            this.button3.Text = "Update";
            this.button3.UseVisualStyleBackColor = true;
            this.button3.Click += new System.EventHandler(this.updateButton_Click);
            // 
            // teammembersTextBox
            // 
            this.teammembersTextBox.Location = new System.Drawing.Point(121, 356);
            this.teammembersTextBox.Name = "teammembersTextBox";
            this.teammembersTextBox.Size = new System.Drawing.Size(100, 22);
            this.teammembersTextBox.TabIndex = 7;
            // 
            // teamyearTextBox
            // 
            this.teamyearTextBox.Location = new System.Drawing.Point(121, 399);
            this.teamyearTextBox.Name = "teamyearTextBox";
            this.teamyearTextBox.Size = new System.Drawing.Size(100, 22);
            this.teamyearTextBox.TabIndex = 8;
            // 
            // teamcityTextBox
            // 
            this.teamcityTextBox.Location = new System.Drawing.Point(392, 320);
            this.teamcityTextBox.Name = "teamcityTextBox";
            this.teamcityTextBox.Size = new System.Drawing.Size(100, 22);
            this.teamcityTextBox.TabIndex = 9;
            // 
            // teamtypeTextBox
            // 
            this.teamtypeTextBox.Location = new System.Drawing.Point(392, 371);
            this.teamtypeTextBox.Name = "teamtypeTextBox";
            this.teamtypeTextBox.Size = new System.Drawing.Size(100, 22);
            this.teamtypeTextBox.TabIndex = 10;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(22, 359);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(82, 16);
            this.label2.TabIndex = 11;
            this.label2.Text = "nb members";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(48, 399);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(34, 16);
            this.label3.TabIndex = 12;
            this.label3.Text = "year";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(333, 320);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(27, 16);
            this.label4.TabIndex = 13;
            this.label4.Text = "city";
            this.label4.Click += new System.EventHandler(this.label4_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(327, 371);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(33, 16);
            this.label5.TabIndex = 14;
            this.label5.Text = "type";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1485, 567);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.teamtypeTextBox);
            this.Controls.Add(this.teamcityTextBox);
            this.Controls.Add(this.teamyearTextBox);
            this.Controls.Add(this.teammembersTextBox);
            this.Controls.Add(this.button3);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.sportDataGridView);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.teamDataGridView);
            this.Controls.Add(this.teamnameTextBox);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.teamDataGridView)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.sportDataGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TextBox teamnameTextBox;
        private System.Windows.Forms.DataGridView teamDataGridView;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataGridView sportDataGridView;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Button button3;
        private System.Windows.Forms.TextBox teammembersTextBox;
        private System.Windows.Forms.TextBox teamyearTextBox;
        private System.Windows.Forms.TextBox teamcityTextBox;
        private System.Windows.Forms.TextBox teamtypeTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
    }
}

