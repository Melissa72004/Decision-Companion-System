from django.shortcuts import render

def chatbot(request):
    response = ""
    best_option = ""

    if request.method == "POST":
        decision = request.POST.get("decision")
        criteria = request.POST.getlist("criteria[]")
        options = request.POST.getlist("option[]")

        scores = {}
        for option in options:
            total = 0
            for criterion in criteria:
                score_name = f"score_{option}_{criterion}"
                score = request.POST.get(score_name)
                if score:
                    total += int(score)
            scores[option] = total

        if scores:
            best_option = max(scores, key=scores.get)
            response = f"✅ Based on your scores, the best option for '{decision}' is: {best_option}"

    return render(request, "chatbot.html", {
        "response": response
    })