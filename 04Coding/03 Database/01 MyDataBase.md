---
title: MyDataBase
date: 2023-08-05 23:59
article: false
tags: 
---

database: [[../../Others/个人档案/database登录|database登录]]
第四题
**Proof:**

Given the definition of \( h(x, \mu) \):
\[ h(x; \mu ) = L(x) + \frac{1}{2\mu} \|c(x)\|_2^2 \]

Taking the gradient with respect to \( x \) and setting it to zero gives:

\[ \nabla L(x) + \mu c(x) = 0 \]

Evaluating at \( x^* \) (given that \( x^* \) minimizes \( h \)), we have:

\[ \nabla L(x^*) + \mu c(x^*) = 0 \]

Since \( c(x^*) = 0 \) (due to the equality constraint), this verifies the first part:

\[ \nabla L(x^*) = 0 \]

Now, consider the Hessian of \( h \) with respect to \( x \). For any direction \( d \) satisfying \( \nabla c(x^*)^T d = 0 \):

\[ d^T \nabla^2 h(x^*) d = d^T \nabla^2 L(x^*) d + \mu d^T c(x^*) \]

Again, due to \( c(x^*) = 0 \), the second term on the right side drops out, leaving:

\[ d^T \nabla^2 L(x^*) d \]

Given the assumption that \( x^* \) minimizes \( h \) for all \( \mu > 0 \), this expression must be non-negative for all valid \( d \), satisfying the second-order KKT condition.

Thus, both the gradient and the second-order conditions for \( L \) at \( x^* \) are satisfied.