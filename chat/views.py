from django.shortcuts import render
from django.http import HttpResponse
from .forms import ServiceForm
import openai






# ここでは商品の内容の整理
def service_definition_view(request):
    chat_results = {"value": "", "similar_services": "", "unique_value": "", "solution": "", "customer": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserと一緒にサービスの内容を考えます。\n"
                            "ユーザーが提案したサービスを整理し答えなさい\n"
                            "以下にそれぞれの項目について回答してください：\n"
                            "サービスの目的:"
                            "サービスの特徴："
                            "サービスのメリット："
                            "以上の項目を一つ回答してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response["choices"][0]["message"]["content"]
            split_responses = chat_response.split("\n")
    
            print(split_responses)

            
            chat_results = {
                "value": split_responses[1],
                "similar_services": split_responses[4],
                "unique_value": split_responses[7],
            }
    else:
        form = ServiceForm()

    return render(request, 'chat/chat.html', {'form': form, 'chat_results': chat_results})


# 顧客定義
def customer_defind_view(request):
    chat_results = {"product": "", "lookalike": "", "unique_value": "", "solution": "", "customer": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、ひとつづつ回答をお願いします\n"
                            "顧客の定義："
                            "顧客価値提供："
                            "ニーズと要求:"
                            "それぞれの項目について、詳細な情報を提供してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")

            print(split_responses)
            
            chat_results = {
                "product": split_responses[0],
                "customer": split_responses[2],
                "lookalike": split_responses[4],
            }
    else:
        form = ServiceForm()

    return render(request, 'chat/product_ideas.html', {'form': form, 'chat_results': chat_results})



def business_composition_view(request):
    chat_results = {"source_of_income": "", "business_model": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、20文字以内で回答をお願いします\n"
                            "収入源："
                            "ビジネスモデル："
                            "それぞれの項目について、詳細な情報を提供してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")

            if len(split_responses) >= 2:
                chat_results = {
                    "source_of_income": split_responses[0].replace("収入源：", "").strip(),
                    "business_model": split_responses[1].replace("ビジネスモデル：", "").strip(),
                }
    else:
        form = ServiceForm()

    return render(request, 'chat/business_composition.html', {'form': form, 'chat_results': chat_results})


def initial_hypothesis_view(request):
    chat_results = {"source_of_income": "", "business_model": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、20文字以内で回答をお願いします\n"
                            "顧客の可視化："
                            "ペルソナの可視化："
                            "それぞれの項目について、詳細な情報を提供してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")

            if len(split_responses) >= 2:
                chat_results = {
                    "source_of_income": split_responses[0].replace("顧客の可視化：", "").strip(),
                    "business_model": split_responses[1].replace("ペルソナの可視化：", "").strip(),
                }
    else:
        form = ServiceForm()

    return render(request, 'chat/initial_hypothesis.html', {'form': form, 'chat_results': chat_results})


def product_ideas_view(request):
    chat_results = {"product": "", "lookalike": "", "unique_value": "", "solution": "", "customer": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、20文字以内で回答をお願いします\n"
                            "顧客の定義："
                            "想定している顧客："
                            "想定している顧客が抱えている課題"
                            "それぞれの項目について、詳細な情報を提供してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")

            print(split_responses)
            
            chat_results = {
                "product": split_responses[0],
                "customer": split_responses[2],
                "lookalike": split_responses[4],
            }
    else:
        form = ServiceForm()

    return render(request, 'chat/product_ideas.html', {'form': form, 'chat_results': chat_results})


def business_composition_view(request):
    chat_results = {"source_of_income": "", "business_model": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、20文字以内で回答をお願いします\n"
                            "収入源："
                            "ビジネスモデル："
                            "それぞれの項目について、詳細な情報を提供してください。"
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")

            if len(split_responses) >= 2:
                chat_results = {
                    "source_of_income": split_responses[0].replace("収入源：", "").strip(),
                    "business_model": split_responses[1].replace("ビジネスモデル：", "").strip(),
                }
    else:
        form = ServiceForm()

    return render(request, 'chat/business_composition.html', {'form': form, 'chat_results': chat_results})


def market_view(request):
    chat_results = {"source_of_income": "", "business_model": ""}
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_details = form.cleaned_data['service_details']

            openai.api_key = "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"

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "あなたはuserが提案した企画に、\n"
                            "アドバイスをするため\n"
                            "以下の項目について、2回答をお願いします\n"
                            "市場の定義："
                            "市場のセグメンテーション："
                            "それぞれの項目について、詳細な情報を提供してください。"
                            
                        )
                    },
                    {
                        "role": "user",
                        "content": service_details
                    },
                ],
            )

            chat_response = response['choices'][-1]['message']['content']
            split_responses = chat_response.split("\n")
            
            print(split_responses)

            if len(split_responses) >= 2:
                chat_results = {
                    "source_of_income": split_responses[0].replace("顧客の可視化：", "").strip(),
                    "business_model": split_responses[1].replace("ペルソナの可視化：", "").strip(),
                }
    else:
        form = ServiceForm()

    return render(request, 'chat/market.html', {'form': form, 'chat_results': chat_results})
