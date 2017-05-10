# Can you see through the stars - Challenge 110

The is a .NET executable so we'll use ILSpy to inspect the code.

```
// crackmeform.Form1
private void button1_Click(object sender, EventArgs e)
{
	this.maskedTextBox1.Text = "FLAG-" + this.maskedTextBox1.Name + "vc" + this.button1.Name;
}
```

We can find all we need in the following bits of code:

```
// crackmeform.Form1
private void InitializeComponent()
{
	this.button1 = new Button();
	this.maskedTextBox1 = new MaskedTextBox();
	base.SuspendLayout();
	Point location = new Point(12, 49);
	this.button1.Location = location;
	this.button1.Name = "button1";
	Size size = new Size(260, 23);
	this.button1.Size = size;
	this.button1.TabIndex = 0;
	this.button1.Text = "Generate Flag";
	this.button1.UseVisualStyleBackColor = true;
	this.button1.Click += new EventHandler(this.button1_Click);
	Point location2 = new Point(13, 13);
	this.maskedTextBox1.Location = location2;
	this.maskedTextBox1.Name = "maskedTextBox1";
	this.maskedTextBox1.PasswordChar = '*';
	this.maskedTextBox1.ReadOnly = true;
	Size size2 = new Size(259, 20);
	this.maskedTextBox1.Size = size2;
	this.maskedTextBox1.TabIndex = 1;
	SizeF autoScaleDimensions = new SizeF(6f, 13f);
	base.AutoScaleDimensions = autoScaleDimensions;
	base.AutoScaleMode = AutoScaleMode.Font;
	Color activeCaptionText = SystemColors.ActiveCaptionText;
	this.BackColor = activeCaptionText;
	Size clientSize = new Size(284, 88);
	base.ClientSize = clientSize;
	base.Controls.Add(this.maskedTextBox1);
	base.Controls.Add(this.button1);
	base.Name = "Form1";
	base.StartPosition = FormStartPosition.CenterScreen;
	this.Text = "CrackMe";
	base.ResumeLayout(false);
	base.PerformLayout();
}
```

FLAG is: FLAG-maskedTextBox1vcbutton1
