from django import forms


class DappForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'id':"name",'type':"text",'placeholder':"enter name",'aria-describeby':"p1"}))

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'id':"email",'type':"email",'placeholder':"enter email",'aria-describeby':"p2"}))

    phonenumber = forms.IntegerField(
        label='Phonenumber',
        widget=forms.NumberInput(attrs={'id':"phonenumber",'type':"number",'placeholder':"enter phonenumber",'aria-describeby':"p3"}))

    description = forms.CharField(
        label='Description',
        max_length=100,
        widget=forms.TextInput(attrs={'id':"description",'type':"text",'placeholder':"enter description",'aria-describeby':"p4"}))


    ename = forms.CharField(max_length=50)
    eemail = forms.CharField(max_length=50)
    ephonenumber = forms.CharField(max_length=50)
    edescription = forms.CharField(max_length=50)



    # def clean_test_name(self):
    #     test_name = self.get('name')

    #     # cleaned_data = super().clean()
    #     # test_name = cleaned_data.get('name')
    #     # test_email = cleaned_data.get('email')
    #     # test_phonenumber = cleaned_data.get('phonenumber')
    #     # test_desccription = cleaned_data.get('description')

    #     if len((test_name)) < 4:
    #         raise forms.ValidationError('Minimum 4 characters required')
    #     return test_phonenumber





    

    