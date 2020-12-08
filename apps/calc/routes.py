from flask import Blueprint, render_template, redirect, request
from flask_login import login_required, logout_user, current_user



calculate = Blueprint('calculate', __name__)

@calculate.route('/calc', methods=['GET','POST'])
@login_required
def calc():
    if request.method == 'POST':
        var1 = request.form.get('var1', type=int)
        var2 = request.form.get('var2', type=int)
        operate = request.form.get('operation')
        if operate == 'add':
            result = var1 + var2
        elif operate == 'sub':
            result = var1 - var2
        elif operate == 'div':
             result = var1 / var2
        elif operate == 'mul':
            result = var1 * var2

        return render_template('result.html', entry=result)
    return render_template('chome.html')

