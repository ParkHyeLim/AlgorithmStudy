def allocate_budget(total_budget, requests):
    # 모든 예산요청의 총합이 국가예산을 초과하는 경우 상한액을 계산
    total_requested = sum(requests)
    if total_requested <= total_budget:
        return requests  # 모든 예산요청을 그대로 배정
    else:
        # 상한액 계산
        upper_limit = max(requests)  # 예산요청 중 가장 큰 값으로 상한액 초기화

        # 이진 탐색을 사용하여 상한액을 조정
        left = 0
        right = upper_limit

        while left <= right:
            mid = (left + right) // 2
            allocated_budget = 0

            # 상한액 이하의 예산요청은 그대로 배정하고, 이상의 예산요청은 상한액으로 배정
            for req in requests:
                allocated_budget += min(mid, req)

            # 상한액을 조정하여 배정 가능한 최대 예산을 찾기 위한 이진 탐색
            if allocated_budget > total_budget:
                right = mid - 1
            else:
                left = mid + 1
                upper_limit = mid

        # 상한액 이하의 예산요청은 그대로 배정하고, 이상의 예산요청은 상한액으로 배정
        allocated_budgets = []
        for req in requests:
            allocated_budgets.append(min(upper_limit, req))

        return allocated_budgets
