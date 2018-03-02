import random
from django.shortcuts import render

def matrix(request):
    matrix_comp = [[5, 5], [5, 5], [3, 2], [3, 4], [5, 2], [5, 0], [0, 3], [0, 3], [0, 4], [4, 4], [6, 6], [0, 5],
                        [3, 3], [3, 2]]
    compet = ["Опыт разработки мобильных приложений под заданную систему", "Владение Java, JavaScript", "Знание Kotlin",
            "Знания цикла разработки, управления памятью",
            "Опыт работы или понимание RxJava, RxAndroid, Retrofit, Dagger2, Android Data Binding", "Знания Android SDK",
            "Знание платформы Cocoa Touch: Objective-C/C, Foundation, UIKit, CoreGraphics, CoreAnimation, QuartzCore, Grand Central Dispatch",
            "Знание Objective-C Runtime", "Владение Swift", "Умение эффективно разрабатывать многопоточные приложения",
            "Знание и владение архитектурой заданной системы", "Знание iOS SDK", "Умение разбираться и работать с чужим кодом",
            "Опыт работы в Agile"]

    user = []
    #user = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    for i in range(len(matrix_comp)):
        user.append(random.randint(0, 6))
    q1 = 0
    q2 = 0
    q11=[]
    q22=[]

    for i in range(len(matrix_comp)):
        for j in range(len(matrix_comp[i])):
            if j % 2 == 0:
                if matrix_comp[i][j] <= user[i]:
                    q1 += 1
                if matrix_comp[i][j] > user[i]:
                    q11.append(i)
            else:
                if matrix_comp[i][j] <= user[i]:
                    q2 += 1
                if matrix_comp[i][j] > user[i]:
                    q22.append(i)

    if q1 > q2:
        print("Вам лучше всего взяться за Андроид-разработку!\n")
        if len(q11) != 0:
            print("Необходимо изучить следующие навыки:")
            for p in range(len(q11)):
                if (matrix_comp[q11[p]][0] - user[q11[p]]) == 2 or (matrix_comp[q11[p]][0] - user[q11[p]]) == 3 or (
                        matrix_comp[q11[p]][0] - user[q11[p]]) == 4:
                    print(str(p+1) + ". " + compet[q11[p]] + " на " + str(matrix_comp[q11[p]][0] - user[q11[p]]) + " уровня")
                elif (matrix_comp[q11[p]][0] - user[q11[p]]) == 1:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q11[p]][0] - user[q11[p]]) + " уровень")
                else:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q11[p]][0] - user[q11[p]]) + " уровней")
        else:
            print("Отлично! Вы изучили все навыки, необходимые для занятия должности Андроид-разработчика")
    elif q1 == q2:
        print("Вы можете взяться и за Андроид-разработку, и за IOS-разработку\n")
        if len(q11) != 0:
            print("Для того, чтобы стать Андроид-разработчиком, вам необходимо изучить следующие навыки:")
            for p in range(len(q11)):
                if (matrix_comp[q11[p]][0] - user[q11[p]]) == 2 or (matrix_comp[q11[p]][0] - user[q11[p]]) == 3 or (
                        matrix_comp[q11[p]][0] - user[q11[p]]) == 4:
                    print(str(p+1) + ". " + compet[q11[p]] + " на " + str(matrix_comp[q11[p]][0] - user[q11[p]]) + " уровня")
                elif (matrix_comp[q11[p]][0] - user[q11[p]]) == 1:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q11[p]][0] - user[q11[p]]) + " уровень")
                else:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q11[p]][0] - user[q11[p]]) + " уровней")

        if len(q22) != 0:
            print("\nДля того, чтобы стать IOS-разработчиком, вам необходимо изучить следующие навыки:")
            for p in range(len(q22)):
                if (matrix_comp[q22[p]][1] - user[q22[p]]) == 2 or (matrix_comp[q22[p]][1] - user[q22[p]]) == 3 or (matrix_comp[q22[p]][1] - user[q22[p]]) == 4:
                    print(str(p+1) + ". " + compet[q11[p]] + " на " + str(matrix_comp[q22[p]][1] - user[q22[p]]) + " уровня")
                elif (matrix_comp[q22[p]][1] - user[q22[p]]) == 1:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q22[p]][1] - user[q22[p]]) + " уровень")
                else:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q22[p]][1] - user[q22[p]]) + " уровней")
        else:
            print("Отлично! Вы изучили все навыки, необходимые для занятия должностей Андроид-разработчика и IOS-разработчика")
    else:
        print("Вам лучше всего взяться за IOS-разработку\n")
        if len(q22) != 0:
            print("Необходимо изучить следующие навыки:")
            for p in range(len(q22)):
                if (matrix_comp[q22[p]][1] - user[q22[p]]) == 2 or (matrix_comp[q22[p]][1] - user[q22[p]]) == 3 or (matrix_comp[q22[p]][1] - user[q22[p]]) == 4:
                    print(str(p+1) + ". " + compet[q11[p]] + " на " + str(matrix_comp[q22[p]][1] - user[q22[p]]) + " уровня")
                elif (matrix_comp[q22[p]][1] - user[q22[p]]) == 1:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q22[p]][1] - user[q22[p]]) + " уровень")
                else:
                    print(str(p + 1) + ". " + compet[q11[p]] + " на " + str(
                        matrix_comp[q22[p]][1] - user[q22[p]]) + " уровней")
        else:
            print("Отлично! Вы изучили все навыки, необходимые для занятия должности IOS-разработчика")
    return render(request, 'matrix/index.html', context)