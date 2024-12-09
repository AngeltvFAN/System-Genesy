            // PROPERTIES
            Button guna = new Button();
            Label label_1 = new Label();
            TextBox keyBox = new TextBox();
            Form ad = new Form();
            // ADS FORM
            ad.BackColor = Color.FromArgb(20,20,20);
            ad.ShowInTaskbar = false;
            ad.ShowIcon = false;
            ad.StartPosition = FormStartPosition.CenterScreen;
            ad.TopMost = true;
            ad.FormBorderStyle = FormBorderStyle.None;
            ad.Text = "dr-system.exe";
            ad.MaximizeBox = false;
            ad.Width = 695;
            ad.Height = 505;

            // UI ELEMENTS / PROPERTIES
            guna.Parent = ad;
            guna.Width = 65;
            guna.Height = 35;
            guna.Location = new Point(428, 222);
            guna.BorderThickness = 1;
            guna.BorderColor = Color.FromArgb(45, 45, 45);
            guna.FillColor = Color.FromArgb(35, 35, 35);
            guna.Animated = true;
            guna.Click += new EventHandler(guna_Click);
            guna.Text = "copy";
            
            void guna_Click(object sender, EventArgs e)
            {
                string c = "passed test.";
                MessageBox.Show(c)
            }
